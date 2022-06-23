def fun(arr,k):
    c=0
    for i in range(len(arr)):
        for j in range(2,arr[i]):
            if(arr[i]%j==0):
                break
        else:
            if(arr[i]!=1 and arr[i]>=k):
                c+=1
    print(c)
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
fun(arr,k)