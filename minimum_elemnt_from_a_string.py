s=input()
l=list(s.split(' '))
s1=l[-1]
k=min(s1)
if k.lower() in s1:
    print(k.lower())
else:
    print(k)
    