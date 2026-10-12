"""fetch.py [v2] PAGE...  (v2: volume 2 of 1845, files q###) : download printed pages (offset 121) to calvin-pages/pNNN.jpg, and a half-size png."""
import sys, os, urllib.request, subprocess
D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "calvin-pages")
args = sys.argv[1:]
V2 = args and args[0] == 'v2'
if V2: args = args[1:]
OFF = int(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'off2.txt')).read()) if V2 else 121
ID = 'institutesofreli02calvuoft' if V2 else 'instituteschrist01calvuoft'
pre = 'q' if V2 else 'p'
for p in args:
    p = int(p)
    f = f"{D}/{pre}{p:03d}.jpg"
    if not os.path.exists(f):
        url = f"https://archive.org/download/{ID}/page/n{p + OFF}_w1600.jpg"
        for attempt in range(3):
            try:
                urllib.request.urlretrieve(url, f)
                break
            except Exception as e:
                print("retry", p, e)
    subprocess.run(["magick", f, "-resize", "60%", f"{D}/{pre}{p:03d}s.png"])
    print(f)
