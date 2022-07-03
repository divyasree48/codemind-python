n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
k=0
for i in range(len(arr)):
    if arr[i]<a or arr[i]>b:
        k+=1
        print(arr[i],end=' ')
if(k==0):
    print(-1)