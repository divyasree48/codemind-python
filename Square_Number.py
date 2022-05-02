n=int(input())
d=0
for i in range(1,n+1):
    if(i*i==n):
        d=1
        break
if(d==1):
    print("True")
else:
    print("False")
    