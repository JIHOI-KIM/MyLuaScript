import os
import sys
import re

S0="-"
S1="-"
S2="-"
SDEPTH="-"
SUMMARY="-"
ERROR=""
TRIPLE="X"

def Do(filename) :

    global S0,S1,S2,SDEPTH
    global SUMMARY, ERROR

    fp = open(filename,'r')
    whole = fp.read()

    sumMsg = re.findall("SUMMARY: AddressSanitizer:.*\(", whole)
    if len(sumMsg) == 0 :
        print( "\n[!] Warning : %s have no ASAN summary..." % filename, end="")
        return False
    
    errMsg = re.findall("ERROR: AddressSanitizer: .*\n", whole)
    if len(errMsg) == 0 :
        print( "\n[!] Warning : %s have no ASAN Error..." % filename, end="")

    stack0Msg = re.findall("#0 [\S]* in [\S]* \(", whole)
    stack1Msg = re.findall("#1 [\S]* in [\S]* \(", whole)
    stack2Msg = re.findall("#2 [\S]* in [\S]* \(", whole)
    stackDMsg = re.findall("#[0-9]* [\S]* in", whole)

    if len(stack0Msg) == 0 :
        print("\n[!] Warning : %s have no stacktrace #0" %filename, end="")
    else :
        L1 = stack0Msg[0].split(" ")
        if len(L1) > 3 :
            L2 = L1[3]
            if S0 == "-" : S0 = L2

    if len(stack1Msg) == 0 :
        print("\n[!] Warning : %s have no stacktrace #1" %filename, end="")
    else :
        L1 = stack1Msg[0].split(" ")
        if len(L1) > 3 :
            L2 = L1[3]
            if S1 == "-" : S1 = L2

    if len(stack2Msg) == 0 :
        print("\n[!] Warning : %s have no stacktrace #2" %filename, end="")
    else :
        L1 = stack2Msg[0].split(" ")
        if len(L1) > 3 :
            L2 = L1[3]
            if S2 == "-" : S2 = L2

    if len(stackDMsg) > 0 :
        try:
            MAX = 0
            for dep in stackDMsg :
                L1 = dep.split(" ")[0].split("#")[1]
                L2 = int(L1)
                if MAX < L2 :
                    MAX = L2
            SDEPTH = "%d" % MAX
        except:
            print("\n[!] Warning : Cannot find stacktrace Depth %s"% filename,  end="")
        

    L1 = sumMsg[0].split(" ")
    if len(L1) > 2 : SUMMARY = L1[-2]

    if SUMMARY == "SEGV" :
        L1 = re.findall("0x[0-9]*",errMsg[0])
        if len(L1) > 0 :
            ERROR =  " (%s)" % L1[0]

    fp.close()
    
fileName = sys.argv[1]
prefix = sys.argv[1].split("/")[-1].split("_")[0]
number = sys.argv[1].split("/")[-1].split("_")[1].split(".")[0].split("crash")[1]

Log1 = Do("temp1.log")
Log2 = Do("temp2.log")
Log3 = Do("temp3.log")

if Log1 :
    if Log2 :
        if Log3 :
            TRIPLE="O"

fp = open("out.csv", "at")

csvline = '\"%s\",\"%s\",\"\",\"%s\",' % (prefix, number, TRIPLE)
csvline += '\"%s%s\",\"%s\",\"\",' % (SUMMARY, ERROR, "X")
csvline += '\"%s\",\"%s\",\"%s\",\"%s\"\n' % (S0, S1, S2, SDEPTH)

fp.write(csvline)

fp.close()
