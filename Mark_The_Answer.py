a,b=map(int,input().split())
arr=list(map(int,input().split()))
s1=s2=0
for i in arr:
    if i<=b:
        s1+=1
    elif i>b:
        if s2==1:
            break
        else:
            s2+=1
print(s1)
