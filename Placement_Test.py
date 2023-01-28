t=int(input())
while(t):
    x,n=map(int,input().split())
    a=x//10
    print(a*n)
    t-=1