n=int(input())
m=-999
while(n):
    r=n%10
    n=n//10
    if(r>m):
        m=r
print(m)