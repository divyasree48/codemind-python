n,m=map(int,input().split())
l=[list(map(int,input().split()))for i in range(n)]
for i in l:
    c=sum(i)
    print(c,end=' ')