// The book downloads (PDFs, EPUBs, print-ready zips) from the R2 bucket, for
// commonwealpress.org: its httpd redirects /files/<book>/<file>.pdf|.epub|.zip here.
//
//   /<release file>            a file by its release name (the-book-v3.pdf): served as it
//                              is, cached for a year (a name never changes its bytes)
//   /files/<book>/<file>       a site link (the-book.pdf, no version): sent on to the
//                              current version's file, by the map the site publishes
//                              (SITE_MAP, /files-map.json: site path -> release name)
//
// Deployed by .github/workflows/files-worker.yml; filled by r2-files.yml.

const YEAR = "public, max-age=31536000, immutable";

export default {
  async fetch(request, env, ctx) {
    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Method not allowed", { status: 405, headers: { allow: "GET, HEAD" } });
    }
    const url = new URL(request.url);
    const path = decodeURIComponent(url.pathname);

    if (path.startsWith("/files/")) {
      const map = await siteMap(env, ctx);
      const name = map && map[path];
      if (!name) return notFound();
      return new Response(null, {
        status: 302,
        // short: the map moves on with each site release
        headers: { location: new URL(`/${encodeURIComponent(name)}`, url).href, "cache-control": "public, max-age=300" },
      });
    }

    const key = path.slice(1);
    if (!key || key.includes("/")) return notFound();
    if (request.method === "HEAD") {
      const head = await env.BOOKS.head(key);
      return head ? new Response(null, { headers: headers(head) }) : notFound();
    }
    const obj = await env.BOOKS.get(key, { range: request.headers, onlyIf: request.headers });
    if (!obj) return notFound();
    const h = headers(obj);
    if (!("body" in obj)) return new Response(null, { status: 304, headers: h }); // If-None-Match held
    if (obj.range && request.headers.has("range")) {
      const { offset = 0, length = obj.size - offset } = "suffix" in obj.range
        ? { offset: obj.size - obj.range.suffix, length: obj.range.suffix } : obj.range;
      h.set("content-range", `bytes ${offset}-${offset + length - 1}/${obj.size}`);
      h.set("content-length", String(length));
      return new Response(obj.body, { status: 206, headers: h });
    }
    return new Response(obj.body, { headers: h });
  },
};

function headers(obj) {
  const h = new Headers();
  obj.writeHttpMetadata(h);
  h.set("etag", obj.httpEtag);
  h.set("cache-control", YEAR);
  h.set("accept-ranges", "bytes");
  h.set("content-length", String(obj.size));
  h.set("access-control-allow-origin", "*");
  // an ebook or a zip is saved, not opened (a link's download attribute does not reach
  // across sites); a PDF opens in the browser
  if (/\.(epub|zip)$/.test(obj.key)) h.set("content-disposition", `attachment; filename="${obj.key}"`);
  return h;
}

function notFound() {
  return new Response("Not found", { status: 404, headers: { "cache-control": "public, max-age=60" } });
}

// The site's map, fetched through Cloudflare's cache (five minutes; only a good answer is
// kept: a 404 cached once broke old links for minutes). When the site cannot give it, the
// last good map: this Worker's, or the copy it keeps in the bucket (MAP_COPY, a key with a
// "/" in it, which no request can reach).
const MAP_COPY = "_site/files-map.json";
let last = null;          // { text, map } in this Worker instance

async function siteMap(env, ctx) {
  try {
    const r = await fetch(env.SITE_MAP, { cf: { cacheTtlByStatus: { "200-299": 300, "300-599": 0 } } });
    if (r.ok) {
      const text = await r.text();
      if (last?.text !== text) {
        const map = JSON.parse(text);
        // the bucket's copy follows the site's (written only when it changes)
        const kept = await env.BOOKS.get(MAP_COPY);
        if (!kept || (await kept.text()) !== text) ctx.waitUntil(env.BOOKS.put(MAP_COPY, text));
        last = { text, map };
      }
      return last.map;
    }
  } catch {
    // the site is down or its answer is not a map: the last good one
  }
  if (last) return last.map;
  const kept = await env.BOOKS.get(MAP_COPY);
  if (!kept) return null;
  const text = await kept.text();
  last = { text, map: JSON.parse(text) };
  return last.map;
}
