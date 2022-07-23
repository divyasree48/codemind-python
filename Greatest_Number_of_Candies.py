n=int(input())
arr=list(map(int,input().split()))
k=int(input())
l=[]
for i in arr:
    if i+k>=max(arr):
        l.append('True')
    else:
        l.append('False')
print(*l)