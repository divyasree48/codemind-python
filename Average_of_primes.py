def fun(arr):
    s=0
    c=0
    for i in range(len(arr)):
        for j in range(2,arr[i]):
            if(arr[i]==1):
                break
            if arr[i]%j==0:
                break
              
        else:
            if(arr[i]!=1):
                s+=arr[i]
                c+=1
    avg=s/c
    print("%.2f"%avg)
n=int(input())
arr=list(map(int,input().split()))
fun(arr)