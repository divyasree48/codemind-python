n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(i+1,n):
        if l[j]>l[i]:
            c+=1
            break
        else:
            c+=1
            if j==n-1 and c>0:
                c=0
                break
    print(c,end=' ')
                