s=input()
inc=0
dec=len(s)
for i in s:
    if i=='I':
        print(inc,end=" ")
        inc+=1
    elif i=='D':
        print(dec,end=" ")
        dec-=1
print(inc)