import glob
from datetime import datetime

filenames = glob.glob("file*.txt")
now = datetime.now()

_str = now.strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"

with open(_str,'w') as outfile:
    for f in filenames:
        with open(f) as f3:
            out = f3.read()
            out = out.splitlines()
            for e in out:
                outfile.write(e+'\n')
