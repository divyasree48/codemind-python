n=int(input())
arr=list(map(int,input().split()))
k=int(input())
s=0
l=0
if(arr[0]>k):
    for i in range(n-1,-1,-1):
        if(arr[i]==k):
            s+=1
            l=i
            break
elif(arr[0]<=k):
    for i in range(len(arr)):
        if(arr[i]==k):
            s+=1
            l=i
            break
if(s==0):
    print(-1)
else:
    print(l)