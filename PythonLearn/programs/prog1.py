
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

N = int(input())
data = [int(x) for x in input().split()]


# Write your code here
# ans = 

final = [];

if (N >=1 and N<= 10**5):
    for i in list(range(N)):
        a = data[i]%10
        final.append(a)
       

prod = 0;
for val in final:
    prod = prod* 10 + val
if (prod % 10) :
    ans = "No";
else :
    ans = "Yes";

print(ans)
