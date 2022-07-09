s=input()
l=list(s.lower())
l1=[]
k=''
for i in l:
    if i==' ':
        continue
    if l.count(i)==1:
        l1.append(i)
for i in sorted(l1):
    k=k+i
print(k)
