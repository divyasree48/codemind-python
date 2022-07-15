s1=input().lower()
s2=input().lower()
l=[]
c=0
for i in s1:
    if i in s2:
        if i==' ':
            continue
        if i not in l:
            l.append(i)
            c+=1
s=''
for i in sorted(l):
    s+=i
if(c==0):
    print(-1)
else:
    print(s)