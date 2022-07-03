n=int(input())
arr=list(map(int,input().split()))
s1=0
s2=0
for i in range(len(arr)//2):
    s1+=arr[i]
for i in range(len(arr)//2,len(arr)):
    s2+=arr[i]
print(s1)
print(s2)