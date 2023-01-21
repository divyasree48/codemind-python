n=int(input())
s=0
while(s!=1 and s!=4):
    s=0
    while(n):
        r=n%10
        s+=r*r
        n//=10
    n=s
if s==1 or s==7:
    print('True')
else:
    print('False')