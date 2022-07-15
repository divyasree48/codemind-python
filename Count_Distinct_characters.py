s=input().lower()
l=list(s.split(' '))
s1=set(s)
if len(l)>1:
    print(len(s1)-1)
else:
    print(len(s1))