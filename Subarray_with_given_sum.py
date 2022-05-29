t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))
    l=0
    c=0
    for j in range(n):
        l=0
        l=l+arr[j]
        for k in range(j+1,n):
            l=l+arr[k]
            if(l==s):
                print(j+1,k+1)
                c+=1
        if(c>0):
            break
    if(c==0):
        print(-1)
                