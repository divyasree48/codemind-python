n=int(input())
arr=list(map(int,input().split()))
k=n-1
d=k//2
i=0
while(i<=k):
    if(n%2!=0):
        if(i!=d and k!=d):
            print(arr[i],arr[k],end=' ')
        if(i==d):
            print(arr[k],end=' ')
            print(0)
        if i>d:
            break
    else:
        print(arr[i],arr[k],end=' ')
    i+=1
    k-=1