n=int(input())
a=n
b=str(n*n)
d=str(n)[::-1]
e=int(d)*int(d)
c=str(e)[::-1]
if b==c:
    print('True')
else:
    print('False')