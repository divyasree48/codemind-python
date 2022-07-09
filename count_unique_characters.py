s=input()
l=list(s.lower())
c=0
for i in l:
    if i==' ':
        continue
    if l.count(i)==1:
        c+=1
print(c)