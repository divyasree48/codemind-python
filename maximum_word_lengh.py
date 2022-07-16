s=input()
l=[]
for i in s.split(' '):
    l.append(len(i))
print(max(l))