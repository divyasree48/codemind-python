n=int(input())
sq=n*n
temp=sq
rev=0
while n:
    r=n%10
    n=n//10
    rev=rev*10+r
sqrev=rev*rev
ss=0
while sqrev:
    r1=sqrev%10
    sqrev//=10
    ss=ss*10+r1
if(ss==sq):
    print('True')
else:
    print('False')