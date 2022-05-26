import math
n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(len(arr)):
   sq=int(math.sqrt(arr[i]))
   if sq*sq==arr[i]:
       l.append(arr[i])
print(sum(l))