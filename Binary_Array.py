n=int(input())
l=list(map(int,input().split()))
f=0
for i in l:
    if i!=0 and i!=1:
        f=1
        break
if f==0:
    print('True')
else:
    print('False')