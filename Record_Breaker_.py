t=int(input())
for s in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    if n==1:
        c+=1
    for i in range(n):
        if i==0:
            if l[i]>l[i+1]:
                c+=1
        elif i==n-1:
            f=0
            for j in range(i):
                if l[i]>l[j]:
                    f=1
                else:
                    f=0
                    break
            if f==1:
                c+=1
        else:
            f=0
            for j in range(i):
                if l[i]>l[j]:
                    f=1
                else:
                    f=0
                    break
            if f==1:
                if l[i]>l[i+1]:
                    c+=1
    print('Case #',end='')
    print(s+1,end=': ')
    print(c)
    