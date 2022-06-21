import math
n=int(input())
t=n
sq=n*n
dc=0
while(t):
    t=t//10
    dc+=1
pw=pow(10,dc)
s=sq%pw
if(s==n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')