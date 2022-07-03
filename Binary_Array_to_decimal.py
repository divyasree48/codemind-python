n=int(input())
arr=list(map(int,input().split()))
s=0
k=len(arr)-1
for i in range(len(arr)):
    s+=((2**k)*arr[i])
    k-=1
print(s)