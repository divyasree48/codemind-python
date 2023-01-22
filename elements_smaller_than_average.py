import math
n=int(input())
l=list(map(int,input().split()))
a=math.floor(sum(l)/len(l))
c=0
for i in l:
    if i<=a:
        c+=1
print(c)