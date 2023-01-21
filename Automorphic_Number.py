import math
n=int(input())
a=n*n
b=len(str(n))
r=n%(pow(10,b))
p=a%(pow(10,b))
if r==p:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')