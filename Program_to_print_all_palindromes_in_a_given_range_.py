s=int(input())
e=int(input())

for i in range(s,e+1):
    j=i;
    k=0
    while(i):
        r=i%10
        i=i//10
        k=k*10+r
    if(k==j):
        print(j,end=' ')
    