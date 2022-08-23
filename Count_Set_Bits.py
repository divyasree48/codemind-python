t=int(input())
while(t):
    n=int(input())
    b=''
    while(n):
        r=n%2
        b=b+str(r)
        n=n//2
    c=0
    for i in b:
        if i=='1':
            c+=1
    print(c)