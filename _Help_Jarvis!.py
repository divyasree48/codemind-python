t=int(input())
for i in range(t):
    n=int(input())
    le=0
    arr=[]
    k=0
    c=0
    te=n
    while(te):
        r=te%10
        le+=1
        arr.append(r)
        k+=1
        te=te//10
    for j in range(0,k):
        for l in range(j+1,k):
            if(arr[j]>arr[l]):
                te=arr[j]
                arr[j]=arr[l]
                arr[l]=te
    for j in range(1,k):
        if(arr[j]-arr[j-1]==1):
            c+=1
    if(c==k-1):
        print('YES')
    else:
        print('NO')