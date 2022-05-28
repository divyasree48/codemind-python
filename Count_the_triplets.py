t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i!=j):
                if arr[i]+arr[j] in arr:
                    c+=1
    if(c==0):
        print(-1)
    else:
        print(c//2)