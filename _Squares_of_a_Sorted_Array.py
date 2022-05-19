n=int(input())
arr=list(map(int,input().split()))
p=[]
for i in range(n):
    p.append(arr[i]*arr[i])
print(*sorted(p))