n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
l=[]
for i in a:
    if i not in b:
        if i not in l:
            l.append(i)
for i in b:
    if i not in a:
        if i not in l:
            l.append(i)
print(len(l))

