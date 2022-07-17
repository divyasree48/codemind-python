s=input()
l=list(s.split(' '))
s1=''
for i in range(len(l)):
    if i!=len(l)-1:
        if i%2==0:
            k=l[i]
            s1+=k[::-1]+' '
        else:
            s1+=l[i]+' '
    else:
        if i%2==0:
            k=l[i]
            s1+=k[::-1]
        else:
            s1+=l[i]
print(s1)        