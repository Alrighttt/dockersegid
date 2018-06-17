#!/usr/bin/python
from list import segids
import subprocess

for e in segids:
  subprocess.call("./dockerstart.sh " + str(e[1]) + " segid" + str(e[0]), shell=True)


