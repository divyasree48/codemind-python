s=input()
v='aeiouAEIOU'
l=[]
c=0
for i in s:
    if i==' ':
        continue
    if i in v:
        if i not in l:
            l.append(i)
            c+=1
if c==0:
    print(-1)
else:
    print(*l,end=' ')