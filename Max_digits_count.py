n=int(input())
arr=list(map(int,input().split()))
a=[]
for i in range(0,len(arr)):
    d=0
    while(arr[i]):
        arr[i]//=10
        d+=1
    a.append(d)
print(a.count(max(a)))