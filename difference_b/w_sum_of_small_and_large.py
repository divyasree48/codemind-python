s=input()
l=list(s.split(' '))
m=n=0
for i in l:
    m+=ord(min(i))
    n+=ord(max(i))
print(n-m)