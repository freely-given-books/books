"""crop.py PAGE Y0 Y1 [X0 X1] : crop full-res page (fraction of height 0-1) to cNNN.png"""
import sys, os, subprocess
D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "calvin-pages")
pre = "q" if sys.argv[1].startswith("q") else "p"
p = int(sys.argv[1].lstrip("q")); y0 = float(sys.argv[2]); y1 = float(sys.argv[3])
x0 = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
x1 = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
f = f"{D}/{pre}{p:03d}.jpg"
out = subprocess.run(["magick", "identify", "-format", "%w %h", f], capture_output=True, text=True).stdout.split()
w, h = int(out[0]), int(out[1])
g = f"{int((x1-x0)*w)}x{int((y1-y0)*h)}+{int(x0*w)}+{int(y0*h)}"
o = f"{D}/c{pre}{p:03d}_{int(y0*100)}.png"
subprocess.run(["magick", f, "-crop", g, "+repage", o])
print(o)
