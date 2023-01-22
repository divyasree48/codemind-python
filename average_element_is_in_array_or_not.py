n=int(input())
l=list(map(int,input().split()))
a=int(sum(l)/len(l))
for i in l:
    if i==a:
        k=1
        break
    else:
        k=0
if k==1:
    print('True')
else:
    print('False')