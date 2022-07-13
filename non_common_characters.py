s1=input().lower()
s2=input().lower()
l=[]
for i in s2:
    if i==' ':
        continue
    if i not in s1:
        l.append(i)
for i in s1:
    if i==' ':
        continue
    if i not in s2:
        l.append(i)
l=sorted(set(l))
k=''
for i in l:
    k+=i
print(k)