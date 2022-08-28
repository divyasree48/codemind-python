t=int(input())
while(t):
    n=int(input())
    s=input()
    k=l=0
    for i in range(n):
        c=s[i]
        k=0
        for j in range(n):
            if(i!=j):
                if(c==s[j]):
                    k+=1
                    break
        if k==0:
            l+=1
            print(c)
            break
    if(l==0):
        print(-1)
                
    t-=1