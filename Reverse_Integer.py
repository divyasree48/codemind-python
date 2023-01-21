n=int(input())
if n<0:
    f=1
    n*=-1
else:
    f=0
a=str(n)
b=a[::-1]
if f==1:
    b='-'+b
c=''
for i in range(len(b)):
    if i==0 and b[i]=='0':
        continue
    if i==1 and b[i]=='0':
        continue
    else:
        c+=b[i]
print(c)