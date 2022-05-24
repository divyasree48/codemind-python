s=input()
s.lower()
l=[]
v=0
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[i]==s[j] and i!=j:
            c+=1
            break
    if c==0:
        v+=1
        l.append(i)
        break
if v==0:
    print(-1)
else:
    print(*l)