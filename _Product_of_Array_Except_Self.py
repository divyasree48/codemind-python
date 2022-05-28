n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    k=1
    for j in range(n):
        if(i!=j):
            k=k*arr[j]
    print(k,end=' ')
        