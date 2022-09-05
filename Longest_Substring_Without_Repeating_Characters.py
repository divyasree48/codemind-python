def fun(s2):
    k=''
    for i in s2:
        k+=i.lower()
    l=[]
    c=0
    for i in k:
        l.append(i)
    for i in l:
        d=0
        for j in l:
            if i==j:
                d+=1
        if d==1:
            c=1
        else:
            c=0
            break
    if c==1:
        return 1
    else:
        return 0
s=input()
s1=''
l=0
for i in range(len(s)):
    s2=''
    for j in range(i,len(s)):
        s2+=s[j]
        if fun(s2)==1:
            if s2 in s:
                if len(s2)>l:
                    s1=s2
                    l=len(s1)
if(len(s1)>=3):
    print(s1)
else:
    print(-1)