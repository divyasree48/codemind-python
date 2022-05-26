t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    s=(n*(n+1))//2
    s1=sum(arr)
    k=s-s1
    print(k)