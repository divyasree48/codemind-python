s1=input().lower()
s2=input().lower()
l=[]
c=0
for i in s1.split(' '):
    if i in s2.split(' '):
        if s1.count(i)==1 and s2.count(i)==1:
            if i==' ':
                continue
            if i not in l:
                l.append(i)
                c+=1
for i in s2.split(' '):
    if i in s1.split(' '):
        if s1.count(i)==1 and s2.count(i)==1:
            if i==' ':
                continue
            if i not in l:
                l.append(i)
                c+=1

print(c)