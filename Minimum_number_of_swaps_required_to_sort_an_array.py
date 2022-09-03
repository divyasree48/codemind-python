n=int(input())
l=list(map(int,input().split()))
s=sorted(l)
c=0
for i in range(n):
    if l[i]!=s[i]:
        c+=1
        ind=l.index(s[i])
        l[i],l[ind]=l[ind],l[i]
print(c)