n,k,x,y=map(int,input().split())
a=k*x
b=n-k
if x<y:
    c=b*x
else:
    c=b*y
print(a+c)