def sd(n):
    temp=n
    k=0
    c=0
    while(n>0):
        d=n%10
        n=n//10
        if d==0:
            return 0
        elif temp%d==0:
            c+=1
        k+=1
    if c==k:
        return 1
    return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if (sd(i)):
        print(i,end=' ')
