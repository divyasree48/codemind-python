n=int(input())
f=0
i=1
k=0
while(k<=n):
    k=2**i
    if k==n:
        f=1
        break
    i+=1
if f==0:
    print("False")
else:
    print("True")
    