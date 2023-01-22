n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(0,n,2):
    if l[i]%2==1:
        f=1
        break
if f==0:
    print('True')
else:
    print('False')