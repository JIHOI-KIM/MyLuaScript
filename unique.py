import csv
import os

items = os.listdir(".")
csvlist = []

for item in items :
    if item.endswith("csv") :
        csvlist.append(item)

print("----- ----- ----- ----- -----")
print("[Merging Unique Crash]")
print("[+] Find %d csv files from this folder." % len(csvlist))

R4_Hash = []
R4_Name = []
R4_Bug = []
R3_Hash = []
R3_Name = []
R3_Bug = []
R2_Hash = []
R2_Name = []
R2_Bug = []
R1_Hash = []
R1_Name = []
R1_Bug = []
R0_Name = []

for csvf in csvlist :
    fp = open(csvf, 'r', encoding='utf-8')
    rdr = csv.reader(fp)

    TEMPSET = []
    TEMPNAME = None
    TEMPBUG = None
    for line in rdr :
        if len(line) == 15 :
            if len(line[7]) == 32 :
                TEMPSET.append(line[7])
                TEMPNAME = line[1] + "_" + line[2]
                TEMPBUG = line[5]
        else :
            if len(TEMPSET) == 4 :
                R4_Hash.append(TEMPSET)
                R4_Name.append(TEMPNAME)
                R4_Bug.append(TEMPBUG)
            elif len(TEMPSET) == 3 :
                R3_Hash.append(TEMPSET)
                R3_Name.append(TEMPNAME)
                R3_Bug.append(TEMPBUG)
            elif len(TEMPSET) == 2 :
                R2_Hash.append(TEMPSET)
                R2_Name.append(TEMPNAME)
                R2_Bug.append(TEMPBUG)
            elif len(TEMPSET) == 1 :
                R1_Hash.append(TEMPSET)
                R1_Name.append(TEMPNAME)
                R1_Bug.append(TEMPBUG)
            else :
                R0_Name.append(TEMPNAME)
            
            TEMPSET = []

    fp.close()


R4Len = len(R4_Name)
R4_WHOLE = {}
for i in range(0,R4Len) :
    Hashes = R4_Hash[i]
    Name = R4_Name[i]
    Bug = R4_Bug[i]
    
    key = ""
    for H in Hashes :
        key = key + H
    key = key + Bug
    
    if key not in R4_WHOLE :
        R4_WHOLE[key] = []

    R4_WHOLE[key].append(Name)
    
R3Len = len(R3_Name)
R3_WHOLE = {}
for i in range(0,R3Len) :
    Hashes = R3_Hash[i]
    Name = R3_Name[i]
    Bug = R3_Bug[i]
    
    key = ""
    for H in Hashes :
        key = key + H
    key = key + Bug
    
    if key not in R3_WHOLE :
        R3_WHOLE[key] = []

    R3_WHOLE[key].append(Name)
    
R2Len = len(R2_Name)
R2_WHOLE = {}
for i in range(0,R2Len) :
    Hashes = R2_Hash[i]
    Name = R2_Name[i]
    Bug = R2_Bug[i]
    
    key = ""
    for H in Hashes :
        key = key + H
    key = key + Bug
    
    if key not in R2_WHOLE :
        R2_WHOLE[key] = []

    R2_WHOLE[key].append(Name)
        
R1Len = len(R1_Name)
R1_WHOLE = {}
for i in range(0,R1Len) :
    Hashes = R1_Hash[i]
    Name = R1_Name[i]
    Bug = R1_Bug[i]
    
    key = ""
    for H in Hashes :
        key = key + H
    key = key + Bug
    
    if key not in R1_WHOLE :
        R1_WHOLE[key] = []

    R1_WHOLE[key].append(Name)
    
R4_WHOLE = sorted(R4_WHOLE.items(), key=lambda x:len(x[1]), reverse = True)
R3_WHOLE = sorted(R3_WHOLE.items(), key=lambda x:len(x[1]), reverse = True)
R2_WHOLE = sorted(R2_WHOLE.items(), key=lambda x:len(x[1]), reverse = True)
R1_WHOLE = sorted(R1_WHOLE.items(), key=lambda x:len(x[1]), reverse = True)


print("[+] Create [unique.csv] file...")
fp = open("unique.csv", "wt")
fp.write('"Test Environment : clang64, gcc64, clang32, gcc32"\n')
headline = '"Hash1","Hash2","Hash3","Hash4","Bug","Number","Items"\n'

print("[+] Merging Rank 4 Crashes...")
fp.write("\nR4: Crash From 4 Environment (%d items)\n" % len(R4_WHOLE))
fp.write(headline)
for pair in R4_WHOLE :
    label = pair[0]
    table = pair[1]

    H1 = label[:32]
    H2 = label[32:64]
    H3 = label[64:96]
    H4 = label[96:128]
    Bug = label[128:]
    
    csvline = '"%s","%s","%s","%s","%s","%s"' % (H1,H2,H3,H4,Bug,len(table))
    fileline = ''
    
    for filename in table :
        fileline = fileline + ',"%s"' % filename
    
    fp.write(csvline + fileline + "\n")
    

print("[+] Merging Rank 3 Crashes...")
fp.write("\nR3: Crash From 3 Environment (%d items)\n" % len(R3_WHOLE))
fp.write(headline)
for pair in R3_WHOLE :
    label = pair[0]
    table = pair[1]

    H1 = label[:32]
    H2 = label[32:64]
    H3 = label[64:96]
    H4 = "-"
    Bug = label[96:]
    
    csvline = '"%s","%s","%s","%s","%s","%s"' % (H1,H2,H3,H4,Bug,len(table))
    fileline = ''
    
    for filename in table :
        fileline = fileline + ',"%s"' % filename
    
    fp.write(csvline + fileline + "\n")
    
print("[+] Merging Rank 2 Crashes...")
fp.write("\nR2: Crash From 2 Environment (%d items)\n" % len(R2_WHOLE))
fp.write(headline)
for pair in R2_WHOLE :
    label = pair[0]
    table = pair[1]

    H1 = label[:32]
    H2 = label[32:64]
    H3 = "-"
    H4 = "-"
    Bug = label[64:]
    
    csvline = '"%s","%s","%s","%s","%s","%s"' % (H1,H2,H3,H4,Bug,len(table))
    fileline = ''
    
    for filename in table :
        fileline = fileline + ',"%s"' % filename
    
    fp.write(csvline + fileline + "\n")
    
    
print("[+] Merging Rank 1 Crashes...")
fp.write("\nR1: Crash From 1 Environment (%d items)\n" % len(R1_WHOLE))
fp.write(headline)
for pair in R1_WHOLE :
    label = pair[0]
    table = pair[1]

    H1 = label[:32]
    H2 = "-"
    H3 = "-"
    H4 = "-"
    Bug = label[32:]
    
    csvline = '"%s","%s","%s","%s","%s","%s"' % (H1,H2,H3,H4,Bug,len(table))
    fileline = ''
    
    for filename in table :
        fileline = fileline + ',"%s"' % filename
    
    fp.write(csvline + fileline + "\n")
    
print("[+] Done. Closes File [unique.csv]")    
fp.close()

print("----- ----- ----- ----- -----")
