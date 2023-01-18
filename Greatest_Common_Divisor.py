n,m=map(int,input().split())
a=min(n,m)
for i in range(1,a+1):
    if n%i==0 and m%i==0:
        hcf=i
print(hcf)