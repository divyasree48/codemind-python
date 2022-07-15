s1=input()
l=list(s1.split())
k=min(l[-1])
if k.lower() in s1:
    print(k.lower())
else:
    print(k)