
# Write your code here
name = str(input())
if (len(name)<= 20):
        zLength = name.count("z")
        oLength = len(name) - zLength
        if (2 * zLength == oLength):
            print("Yes")
        else :
            print("No")
