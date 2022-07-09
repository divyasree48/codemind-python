s=input()
l=list(s.lower())
l1=[]
for i in l:
    if i==' ':
        continue
    if i not in l1:
        l1.append(i)
print(len(l1))