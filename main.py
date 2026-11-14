import os
import shutil
import sys

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

# High-resolution news summary broadsheet generator for 13 November 2026
src = os.path.join(os.path.dirname(__file__), "entry.png")
dst = os.path.join(out_dir, "entry.png")

shutil.copyfile(src, dst)
print(f"Successfully generated {dst} from {src}")
