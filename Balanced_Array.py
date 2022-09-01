t=int(input())
for a in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    m=0
    for i in range(0,n):
        s1=s2=0
        for j in range(0,i):
            s1+=l[j]
        for k in range(i+1,n):
            s2+=l[k]
        #print(s1,s2)
        if s1==s2:
            m=1
            break
    if m==1:
        print('YES')
    else:
        print("NO")
            