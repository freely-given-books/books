// The book downloads (PDFs, EPUBs, print-ready zips) and the covers (front PNGs, wrap
// WebPs, linked by the site by their release names) from the R2 bucket, for
// commonwealpress.org: its httpd redirects /files/<book>/<file>.pdf|.epub|.zip here.
//
//   /files/<book>/<file>       the site's link (the-book.pdf, no version, the same from
//                              one version to the next): the current version's file,
//                              found by the map the site publishes (SITE_MAP,
//                              /files-map.json: site path -> release name), served
//                              under that name, cached for an hour
//   /<release file>            a file by its release name (the-book-v3.pdf): cached for
//                              a year (a name never changes its bytes)
//
// Deployed by .github/workflows/files-worker.yml; filled by r2-files.yml.

const YEAR = "public, max-age=31536000, immutable";
const HOUR = "public, max-age=3600";

export default {
  async fetch(request, env, ctx) {
    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Method not allowed", { status: 405, headers: { allow: "GET, HEAD" } });
    }
    const path = decodeURIComponent(new URL(request.url).pathname);

    if (path.startsWith("/files/")) {
      const map = await siteMap(env, ctx);
      const key = map && map[path];
      if (!key) return notFound();
      // the map moves on with each release: an hour, and the ETag says when it has
      return serve(request, env, key, HOUR, path.slice(path.lastIndexOf("/") + 1));
    }

    const key = path.slice(1);
    if (!key || key.includes("/")) return notFound();
    return serve(request, env, key, YEAR, key);
  },
};

async function serve(request, env, key, cache, filename) {
  if (request.method === "HEAD") {
    const head = await env.BOOKS.head(key);
    return head ? new Response(null, { headers: headers(head, cache, filename) }) : notFound();
  }
  const obj = await env.BOOKS.get(key, { range: request.headers, onlyIf: request.headers });
  if (!obj) return notFound();
  const h = headers(obj, cache, filename);
  if (!("body" in obj)) return new Response(null, { status: 304, headers: h }); // If-None-Match held
  if (obj.range && request.headers.has("range")) {
    const { offset = 0, length = obj.size - offset } = "suffix" in obj.range
      ? { offset: obj.size - obj.range.suffix, length: obj.range.suffix } : obj.range;
    h.set("content-range", `bytes ${offset}-${offset + length - 1}/${obj.size}`);
    h.set("content-length", String(length));
    return new Response(obj.body, { status: 206, headers: h });
  }
  return new Response(obj.body, { headers: h });
}

function headers(obj, cache, filename) {
  const h = new Headers();
  obj.writeHttpMetadata(h);
  h.set("etag", obj.httpEtag);
  h.set("cache-control", cache);
  h.set("accept-ranges", "bytes");
  h.set("content-length", String(obj.size));
  h.set("access-control-allow-origin", "*");
  // saved under the name it was asked for; an ebook or a zip is saved, not opened (a
  // link's download attribute does not reach across sites), a PDF opens in the browser
  const how = /\.(epub|zip)$/.test(filename) ? "attachment" : "inline";
  h.set("content-disposition", `${how}; filename="${filename}"`);
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
