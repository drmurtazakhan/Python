#!/usr/bin/env python3

import shutil
import os

# sourcedir = "/path/to/sourcedir"
sourcedir = "C:\\tmp2"
# prefix = "tumor_0"
prefix = "0"
extension = "mat"

files = [(f, f[f.rfind("."):], f[:f.rfind(".")].replace(prefix, "")) for f in os.listdir(sourcedir) if f.endswith(extension)]
maxlen = len(max([f[2] for f in files], key = len))

for item in files:
    zeros = maxlen - len(item[2])
    shutil.move(sourcedir+"/"+item[0], sourcedir+"/"+prefix+str(zeros*"0"+item[2])+item[1])