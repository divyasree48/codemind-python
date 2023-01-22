n=int(input())
l=list(map(int,input().split()))
a=l[0]
b=l[1]
l.append(a)
l.append(b)
c=0
for i in range(1,len(l)-1):
    if l[i-1]%2==l[i+1]%2:
        continue
    else:
        c+=1
print(c)