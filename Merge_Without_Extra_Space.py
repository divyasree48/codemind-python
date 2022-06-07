for i in range(int(input())):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    arr1=list(map(int,input().split()))
    new=arr+arr1
    new.sort()
    print(*new)