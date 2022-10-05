n=int(input())
l=list(map(int,input().split()))
if n%2==1:
    a=(n+1)//2
else:
    a=n//2
s=[]
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
i=j=0
while(i<len(e) and j<len(o)):
    
    s.append(o[j])
    s.append(e[i])
    i+=1
    j+=1

while(j<len(o)):
    s.append(o[j])
    j+=1
while(i<len(e)):
    s.append(e[i])
    i+=1
if len(s)%2==1:
    s.append(0)
print(*s)