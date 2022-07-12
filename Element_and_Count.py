n=int(input())
arr=list(map(int,input().split()))
s=[]
for i in arr:
    if i not in s:
        print(i,arr.count(i),end=' ')
        s.append(i)