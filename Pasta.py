n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
c=0
if m>n:
    print("No")
else:
    for i in b:
        if i in a:
            if i not in l:
                l.append(i)
                c+=1
    if len(b)==c:
        print('Yes')
    else:
        print("No")