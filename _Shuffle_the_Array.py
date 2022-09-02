n=int(input())
l=list(map(int,input().split()))
k=n//2
for i in range(k):
    print(l[i],l[k+i],end=' ')