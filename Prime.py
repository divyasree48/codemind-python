import math
n=int(input())
c=1
for i in range(1,int(pow(n,0.5))+1):
    if n%i==0:
        c+=1
if c==2:
    print('Prime')
else:
    print('Not Prime')