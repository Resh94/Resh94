#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/

name = str(input())
if (len(name)<= 20):
    if(name.find("z")== 0 and name.find("o", -1) == len(name) - 1 ):
        begS = name.find("o")
        zString = name[:begS]
        oString = name[begS:]
        zLength = len(zString)
        oLength = len(oString)
        if (2 * zLength == oLength):
            print("Yes")
        else :
            print("No")
