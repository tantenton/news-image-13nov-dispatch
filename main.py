import os
import shutil
import sys

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

src = os.path.join(os.path.dirname(__file__), "entry.png")
dst = os.path.join(out_dir, "entry.png")

shutil.copyfile(src, dst)
print(f"Successfully copied {src} to {dst}")
