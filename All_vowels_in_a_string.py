s=input()
v='aeiou'
l=[]
for i in s:
    if i==' ':
        continue
    if i in v:
        l.append(i)
c=0
for i in v:
    if i not in l:
        c=1
        break
if c==0:
    print('True')
else:
    print('False')