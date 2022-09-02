t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=1
    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            c+=1
    print(c)
    t-=1