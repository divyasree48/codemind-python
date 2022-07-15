s1=input().lower()
s2=input().lower()
c=0
l=[]
for i in s1:
    if i==' ':
        continue
    if i in s2:
        if i not in l:
            l.append(i)
            c+=1
for i in s2:
    if i==' ':
        continue
    if i in s1:
        if i not in l:
            l.append(i)
            c+=1

print(c)