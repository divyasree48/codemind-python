s=input().lower()
l=[]
c=0
for i in s:
    if i==' ':
        continue
    if s.count(i)==1:
        if i not in l:
            l.append(i)
            c+=1
s1=''
for i in sorted(l):
    s1+=i
if c==0:
    print(-1)
else:
    print(s1)