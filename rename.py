import os
import sys

prefix = ""
if (len(sys.argv) != 2) and (len(sys.argv) != 3) :
    print("Usage: python script.py [crashDirectory] [optional:PREFIX]")
    exit()

if len(sys.argv) == 3 :
    print("SET PREFIX : %s" % sys.argv[2])
    prefix = sys.argv[2] + "_"

crashdir = sys.argv[1]
items = os.listdir(crashdir)

for item in items :
    ori = os.path.join(crashdir, item)
    
    v1 = item.split(":")
		# You have to change ":", if another encoding used for file name.
    if len(v1) < 2 :
       continue 

    v2 = v1[1].split(",")
    if len(v2) < 2:
        continue

    try :
        v3 = int(v2[0])
    except :
        print("Cannot parse filename %s" % item)
        continue

    newname = prefix + "crash%05d" % v3 +'.lua'
    after = os.path.join(crashdir,newname)

    os.rename(ori, after)

print("DONE.")
