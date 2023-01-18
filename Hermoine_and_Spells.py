a,b,c=map(int,input().split())
l=[]
l.append(a)
l.append(b)
l.append(c)
s=sorted(l)
print(s[-1]+s[-2])