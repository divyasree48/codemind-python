t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    rev=[]
    l=[]
    for j in range(n-1,-1,-1):
        rev.append(arr[j])
    for k in range(0,n,1):
        if k%2==0:
            l.append(rev[k//2])
        elif k%2==1:
            l.append(arr[k//2])
    print(*l)
            
        