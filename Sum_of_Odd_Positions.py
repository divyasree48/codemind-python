n=int(input())
l=list(map(int,input().split()))

f=g=0
for i in range(n):
    if i%2==1:
        f+=l[i]
print(f)