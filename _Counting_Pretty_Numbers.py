t=int(input())
while(t):
    l,r=map(int,input().split())
    c=0
    for j in range(l,r+1):
        if(j%10==2 or j%10==3 or j%10==9):
            c+=1
    print(c)
    t-=1