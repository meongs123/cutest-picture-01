# The picture ships in the repo as art.jpg (a baby red panda hugging a chick);
# the program only copies it to the output.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "art.jpg"), os.path.join(OUT, "entry.png"))
