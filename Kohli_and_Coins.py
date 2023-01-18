n=int(input())
if n%5==0:
    a=n//10
    b=n%10
    c=b//5
    print(a+c)
else:
    print(-1)