n=int(input())
arr=list(map(int,input().split()))
k=sum(arr)//len(arr)
c=0
for i in arr:
    if i>=k:
        c+=1
print(c)