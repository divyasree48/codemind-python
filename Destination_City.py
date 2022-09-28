n=int(input())
l=[]
for i in range(n):
    k=input()
    l.append(k)
s=l[n-1]
i=s.index(' ')
#print(c)
#print(i)
print(s[i+1::])