n,a,b=map(int,input().split())
for i in range(a,b+1):
    print(n,end=" ")
    print("x",end=" ")
    print(i,end=" = ")
    print(n*i)