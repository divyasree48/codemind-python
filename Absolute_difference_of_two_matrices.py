n=int(input())
a=[list(map(int,input().split()))for i in range(n)]
b=[list(map(int,input().split()))for i in range(n)]
for i in range(n):
    l=[]
    for j in range(n):
        if(a[i][j]>b[i][j]):
            l.append(a[i][j]-b[i][j])
        else:
            l.append(b[i][j]-a[i][j])
    print(*l)