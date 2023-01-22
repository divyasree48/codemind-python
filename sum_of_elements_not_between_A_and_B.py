n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in l:
    if i<a or i>b:
        c.append(i)
if len(c)==0:
    print(0)
else:
    print(sum(c))