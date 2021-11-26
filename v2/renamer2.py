import sys
import os
import shutil

if len(sys.argv) < 2 :
    print("Usage : python3 renamer2.py [OUT_DIR]\n")
    print("for each folder in current DIR, [DIRNAME][SRC]_[NUMBER].lua")

def getSrc(name) :
    L1 = name.split("src:")
    L2 = L1[1]
    L3 = L2.split(",")
    L4 = L3[0]
    return L4[1:]


OUT_DIR = sys.argv[1]
if not os.path.isdir(OUT_DIR) :
    os.mkdir(OUT_DIR)

current = os.listdir(".")
target_folders = []
for item in current :
    if os.path.isdir(item) :
        target_folders.append(item)

for item in target_folders :
    PREFIX = item
    files = []
    bag = {}

    for v in os.listdir(item) :
        if v.startswith("id") :
            files.append(v)

    for name in files :
        tag = item + getSrc(name)
        try:
            bag[tag].append(name) 
        except:
            bag[tag] = []

    for key in bag :
        val_list = bag[key]
        for i in range(0,len(val_list)) :
            new_name = key + "_" + "crash%05d.lua" % i
            origin_name = val_list[i]
            out_name = os.path.join(OUT_DIR, new_name)
            keydir = key[:-5]
            in_name = os.path.join(keydir, origin_name)
            
            shutil.copy(in_name, out_name)





