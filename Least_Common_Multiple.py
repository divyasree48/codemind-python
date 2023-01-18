n,m=map(int,input().split())
a=max(n,m)
b=a
while(1):
    if a%n==0 and a%m==0:
        print(a)
        break
    a+=b
        