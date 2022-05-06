t=int(input())
while(t):
    n,m=map(int,input().split())
    a=-1
    for i in range(0,m+1):
        if((i*i)%m==n):
            a=i
            break
    print(a)
t=t-1