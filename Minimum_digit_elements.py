n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(0,len(arr)):
    if(arr[i]<0):
        arr[i]=-arr[i]
    arr[i]=str(arr[i])
    l.append(len(arr[i]))
print(l.count(min(l)))