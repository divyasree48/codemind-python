s=input().lower()
v='aeiou'
l=[]
for i in v:
    if i not in s:
        if i not in l:
            l.append(i)
k=len(l)
if k>0:
    print(*l)
else:
    print(0)