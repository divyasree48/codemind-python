n=int(input())
arr=list(map(int,input().split()))
p=[]
p=sorted(list(set(arr)))
if(n>=3):
    print(p[-3])
else:
    print(max(p))