s=input()
s1,s2=s.split()
l=[]
for i in s2:
    l.append(i)
flag=0
for i in s1:
    if i in l:
        flag=1
        l.remove(i)
    else:
        flag=0
        break
if flag==1:
    print("True")
else:
    print("False")