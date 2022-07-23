n=int(input())
arr=list(map(int,input().split()))
b=[]
for i in range(1,n+1):
    b.append(i)
for i in b:
    if i not in arr:
        print(i)
        break