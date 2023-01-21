n=int(input())
s=0
p=1
while(n):
    r=n%10
    s+=r
    p*=r
    n=n//10
if p>s:
    print(p-s)
else:
    print(s-p)