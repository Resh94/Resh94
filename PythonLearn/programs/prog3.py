#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisibe-or-2d8e196a/
def solve (A):
    A = list(A)
    arrlen = len(A)
   
    if arrlen%2 == 0 and 1 <= arrlen <= 10**5:
        firsthalf=A[:int(len(A)/2)]
        secondhalf=A[int(len(A)/2):] 
        prod = ""
        prod2 = ""
        for num, num2 in zip(firsthalf, secondhalf):
            if 1<= num <= 10**5 and 1<= num2 <= 10**5 :
                numstr = str(num)
                numstr2 = str(num2)
                prod = prod + numstr[0]
                prod2 = prod2 + numstr2[len(numstr2)-1]     
        prod = prod + prod2
                
        if int(prod) % 11:
            return('NON')
        else :
            return('OUI')

N = int(input())
A = map(int, input().split())
out_ = solve(A)
print (out_)
