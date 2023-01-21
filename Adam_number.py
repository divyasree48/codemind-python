a=int(input())
b=int(str(a)[::-1])
c=str(a*a)
d=str(b*b)
if c==d[::-1]:
    print('True')
else:
    print('False')
