'''
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/split-house-547be0e9/


name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
line = str(input())

if (1<= n <= 20 and len(line) == n):
    if("HH" in line ):
        print('NO')
    elif("." in line):
        res = line.replace('.','B')
        print('YES')
        print(res)
    elif(len(line)==1):
        print("YES")
        print(line)
    else:
        print("NO")
