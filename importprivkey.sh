#!/usr/bin/python
from list import segids
import subprocess

for e in segids:
  subprocess.call("./kmdcli " + str(e[0]) + " importprivkey " + str(e[2]), shell=True)
