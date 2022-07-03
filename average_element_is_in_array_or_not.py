n=int(input())
arr=list(map(int,input().split()))
k=sum(arr)//len(arr)
if k in arr:
    print('True')
else:
    print('False')