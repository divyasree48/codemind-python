n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
    a=l[0]
    for j in range(n-1):
        l[j]=l[j+1]
    l[n-1]=a
for i in l:
    print(i,end=" ")
