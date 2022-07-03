n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for i in range(len(arr)):
   if arr[i]<a or arr[i]>b:
       l.append(arr[i])
if(len(l)>0):
    print(min(l))
else:
    print(-1)