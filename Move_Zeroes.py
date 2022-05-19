n=int(input())
arr=list(map(int,input().split()))
p=[]
c=0
for i in range(n):
    if(arr[i]==0):
        c+=1
    else:
        p.append(arr[i])
for i in range(c):
    p.append(0)
print(*p)
