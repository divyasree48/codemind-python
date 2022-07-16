s1=input().lower()
s2=input().lower()
l=[]
for i in s1:
    if i in s2:
        if i==' ':
            continue
        if i not in l:
            l.append(i)
s=''
for i in sorted(l):
    s+=i
if(len(l)==0):
    print(-1)
else:
    print(s)