n,m=map(int,input().split())
l=[list(map(int,input().split()))for i in range(n)]
c=0
for i in range(n):
    for j in range(m):
        if i==0 or i==n-1:
            c+=l[i][j]
            #print(l[i][j])
        else:
            if j==0 or j==m-1:
                c+=l[i][j]
                #print(l[i][j])
print(c)