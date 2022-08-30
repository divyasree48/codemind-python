n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=x=y=0
for i in a:
    if i==-1:
        c+=1
    else:
        x+=i
for i in b:
    if i==-1:
        c+=1
    else:
        y+=i
if c==2:
    print("Infinite")
else:
    k=0
    for i in range(1000):
        if i+x==y:
            k+=1
print(k)