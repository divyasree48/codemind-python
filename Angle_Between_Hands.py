h,m=map(int,input().split(':'))
a=(h*30-(11*m)/2.0)
if(a>0):
    a=a+0
else:
    a=-a
if(a<(360-a)):
    if(a>int(a)):
        print('{0:.1f}'.format(a))
    else:
        print('{0:.1f}'.format(float(a)))
else:
    if(360-a>int(360-a)):
        print('{0:.1f}'.format(360-a))
    else:
        print('{0:.1f}'.format(float(360-a)))
        