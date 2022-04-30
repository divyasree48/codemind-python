d=0
n=int(input())
for i in range(1,n//2):
    if(i*i==n):
        d+=1
if(d==1):
    print('True')
else:
    print('False')