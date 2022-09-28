n=int(input())
p=[]
h=[]
for i in range(n):
    l=int(input())
    p.append(l)
for i in range(n):
    l=int(input())
    h.append(l)
for i in range(n):
    if p[i]<=h[i]:
        p[i]=0
        h[i]=0
    else:
        if i-1>=0:
            if h[i-1]>p[i]:
                h[i-1]=0
                p[i]=0
        elif i+1<=n:
            if h[i+1]>p[i]:
                h[i+1]=0
                p[i]=0
c=0
for i in p:
    if i!=0:
        c+=1
print(c)