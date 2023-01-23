n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=sorted(list(set(l)))
a=s[::-1]
#print(a)
print(a[k-1])