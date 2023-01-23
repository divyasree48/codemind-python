n=int(input())
l=list(map(int,input().split()))
s=sorted(list(set(l)))
print(s[-2])