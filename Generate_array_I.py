n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(len(arr)):
    if(i%2==0):
        c=1
        while(c<=arr[i+1]):
            l.append(arr[i])
            c+=1
    else:
        continue
print(*l)