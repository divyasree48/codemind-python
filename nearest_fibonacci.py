def fun(n):
    a=0
    b=1
    c=a+b
    i=3
    arr=[]
    while(c<n):
        k=c
        a=b
        b=c
        c=a+b
    arr.append(k)
    arr.append(c)
    return arr
n=int(input())
p=[]
p=fun(n)
if (n-p[0]==p[1]-n):
    print(p[0],p[1])
elif (n-p[0]>p[1]-n):
    print(p[1])
else:
    print(p[0])