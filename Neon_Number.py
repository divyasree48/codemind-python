n=int(input())
s=0
a=n
b=n*n
while(b):
    r=b%10
    s+=r
    b//=10
if s==a:
    print('Neon Number')
else:
    print('Not Neon Number')