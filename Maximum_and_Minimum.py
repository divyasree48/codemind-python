n=int(input())
l=list(map(int,input().split()))
s=set(l)
a=[]
for i in s:
    if l.count(i)==i:
        a.append(i)
if len(a)==0:
    print(-1)
else:
    print(min(a),max(a))