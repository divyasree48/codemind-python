n=int(input())
s=0
temp=n
while n:
    r=n%10
    n=n//10
    s=s*10+r
if(s==temp):
    print('True')
else:
    print('False')