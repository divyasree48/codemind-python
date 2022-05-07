n=int(input())
s=0
arr=list(map(int,input().split()))
for i in range(n):
    s=s+arr[i]
print(s)