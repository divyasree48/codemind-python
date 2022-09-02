n=int(input())
l=list(map(int,input().split()))
m=0
for i in range(n):
    for j in range(i,n):
        if m<l[j]-l[i]:
            m=l[j]-l[i]
print(m)