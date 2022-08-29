s=input()
t=input()
a=[]
b=[]
for i in s:
    if i=='#':
        a.pop()
    else:
        a.append(i)
for i in t:
    if i=='#':
        b.pop()
    else:
        b.append(i)
if a==b:
    print('True')
else:
    print('False')