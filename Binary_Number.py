def bin(n):
    s=""
    while n>0:
        r=n%2
        s+=str(r)
        n//=2
    return s[::-1]
n=int(input())
for i in range(2**n):
    s=bin(i)
    if len(s)!=n:
        for j in range(n-len(s)):
            print("0",end="")
        print(s)
    else:
        print(s)