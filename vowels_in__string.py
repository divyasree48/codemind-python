s=input()
v='aeiouAEIOU'
l=[]
for i in s:
    if i in v:
        if i not in l:
            l.append(i)
k=len(l)
if k>0:
    print(*l)
else:
    print(-1)