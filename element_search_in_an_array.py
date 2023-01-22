n=int(input())
l=list(map(int,input().split()))
k=int(input())
f=g=0
for i in range(n):
    if l[i]==k:
        f+=1
        break
if f==1:
    print('True')
else:
    print('False')