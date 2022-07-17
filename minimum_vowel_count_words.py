s=input()
cnt=[]
v='aeiouAEIOU'
l=list(s.split(' '))
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    cnt.append(c)
m=min(cnt)
k=0
for i in cnt:
    if i==m:
        k+=1
print(k)