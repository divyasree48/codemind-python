n=int(input())
while(n):
    t,m=map(int,input().split())
    a=list(map(int,input().split()))
    while(m):
        x=a[t-1]
        for k in range(t-2,-1,-1):
            a[k+1]=a[k]
        a[0]=x
        m-=1
    print(*a)
    n-=1

        
        
   