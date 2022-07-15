s1=input().lower()
s2=input().lower()
l=[]
for i in s2.split(' '):
    if i in s1.split(' '):
        l.append(i)
for i in range(len(l)):
    if i==len(l)-1:
        print(l[i])
    else:
        print(l[i],end=' ')