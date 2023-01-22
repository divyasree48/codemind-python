import math
n=int(input())
l=list(map(int,input().split()))
c=0
a=math.floor(sum(l)/len(l))
for i in l:
    if i>=a:
        c+=1
print(c)