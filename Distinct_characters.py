s=input().lower()
s=sorted(set(s))
s1=''
for i in s:
    if i==' ':
        continue
    else:
        s1+=i
print(s1)