s=input()
l=list(sorted(s.split(' ')))
s1=''
for i in range(len(l)):
    if(i==len(l)-1):
        s1+=l[i]
    else:
        s1+=l[i]+' '
print(s1)