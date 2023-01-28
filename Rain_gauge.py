t=int(input())
while(t):
    n=int(input())
    if n<3:
        print('LIGHT')
    elif n>=3 and n<7:
        print('MODERATE')
    else:
        print('HEAVY')
    t-=1