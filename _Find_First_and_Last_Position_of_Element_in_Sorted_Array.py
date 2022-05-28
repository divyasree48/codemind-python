n=int(input())
arr=list(map(int,input().split()))
k=int(input())
s=0
l=0
f=0
for i in range(len(arr)):
    if(arr[i]==k):
        s+=1
        f=i
        break
for i in range(f+1,len(arr)):
    if(arr[i]==k):
        s+=1
        l=i
        break
if(s==0):
    print(-1,-1)
else:
    print(f,l)
