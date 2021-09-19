import sys
import os
import shutil

if len(sys.argv) != 3 :
    print("USAGE : python script.py [DIRNAME] [INIT NUM]")
    exit()

files_t = os.listdir(sys.argv[1])
files = sorted(files_t)
init_num = int(sys.argv[2])

dirs = []

if len(files) < init_num :
    print("ERROR : INIT NUMBER < number of files")
    os.exit()

now = init_num
dirs.append(files[0:init_num])

while (now + 100) < len(files) :
    dirs.append(files[now:now+100])
    now = now+100

if now < len(files) :
    dirs.append(files[now:len(files)])

for i in range(len(dirs)) :
    os.mkdir("DIR%d" % i)

count = 0
for dir_t in dirs :
    print(len(dir_t))
    for filename in dir_t :
        origin = os.path.join(sys.argv[1], filename)
        destination = os.path.join("DIR%d" % count, filename)
        shutil.copy(origin, destination)
    count = count+1

print("DONE. (%d Directories)\n" % len(dirs))

