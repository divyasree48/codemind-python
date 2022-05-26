def fun(n):
    arr=[]
    k=0
    while(n):
        r=n%10
        n=n//10
        arr.append(r)
    if(len(arr)>1):
        for i in range(len(arr)):
            k=k+arr[i]
    if(len(arr)==1):
        print(*arr)
    return fun(k)
            
n=int(input())
fun(n)