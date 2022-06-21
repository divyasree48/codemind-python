n=int(input())
arr=list(map(int,input().split()))
a=[]
for i in range(0,len(arr)):
    d=0
    f=0
    if(arr[i]<0):
        arr[i]=-arr[i]
        f=1
    temp=arr[i]
    if(arr[i]==0):
        d=1
    while(arr[i]):
        arr[i]//=10
        d+=1
    a.append(d)
    arr[i]=temp
    if(f==1):
        arr[i]=-arr[i]
k=max(a)
for i in range(n):
    d=0
    f=0
    if(arr[i]<0):
        arr[i]=-arr[i]
        f=1
    temp=arr[i]
    if(arr[i]==0):
        d=1
    while(arr[i]):
        arr[i]=arr[i]//10
        d+=1
    a.append(d)
    arr[i]=temp
    if(f==1):
        temp=-temp
    if(d==k):
        print(temp,end=' ')
        