s1=input().lower()
s2=input().lower()
c=0
l=[]

for i in s1:
    if i==' ':
        continue
    if i not in s2:
        if i not in l:
            l.append(i)
            c+=1
for i in s2:
    if i==' ':
        continue
    if i not in s1:
        if i not in l:
            l.append(i)
            c+=1
if c==0:
    print(-1)
else:
    print(c)