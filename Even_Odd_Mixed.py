n=int(input())
a=b=c=0
while(n):
    c+=1
    r=n%10
    n=n//10
    if r%2==0:
        a+=1
    else:
        b+=1
if a==c:
    print('Even')
elif b==c:
    print('Odd')
else:
    print('Mixed')