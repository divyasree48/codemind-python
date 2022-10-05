s=input().lower()
v='aeiou'
c=0
for i in s.split(' '):
    l=len(i)
    for j in range(len(i)//2):
        if i[j] in v:
            if i[l-j-1] not in v:
                c+=1
        if i[j] not in v:
            if i[l-j-1] in v:
                c+=1
print(c)
        