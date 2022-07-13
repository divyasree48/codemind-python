s=input().lower()
l=[]
s1=''
for i in s:
    if i==' ':
        continue
    if i not in l:
        l.append(i)
for i in sorted(l):
    s1+=i
print(s1)