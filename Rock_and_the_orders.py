d,c=map(int,input().split())
a1,a2,a3=map(int,input().split())
b1,b2,b3=map(int,input().split())
s1=a1+a2+a3
s2=b1+b2+b3
if s1>=150 and s2>=150:
    wc=s1+s2+c
    woc=s1+s2+(2*d)
elif (s1>=150 and s2<150) or (s1<150 and s2>=150):
    wc=s1+s2+c+d
    woc=s1+s2+(2*d)
else:
    wc=s1+s2+c+d+d
    woc=s1+s2+d+d
if wc<woc:
    print('YES')
else:
    print('NO')
