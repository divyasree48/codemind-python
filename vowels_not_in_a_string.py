s=input().lower()
v='aeiou'
l=[]
s1=''
for i in s:
    if i in v:
        s1+=i
for i in v:
    if i not in s1:
        l.append(i)
if len(l)==0:
    print(0)
else:
    print(*l)
        