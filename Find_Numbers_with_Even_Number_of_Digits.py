n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    d=0
    while(arr[i]):
        d+=1
        arr[i]=arr[i]//10
    if(d%2==0):
        c+=1
print(c)
        