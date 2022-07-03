n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(0,len(arr),2):
    if arr[i]%2!=0:
        c+=1
if(c==0):
    print('True')
else:
    print('False')