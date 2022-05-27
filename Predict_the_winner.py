n=int(input())
arr=list(map(int,input().split()))
x=0
y=0
for i in range(len(arr)):
    if(i%2==0):
        x=x+arr[i]
    else:
        y=y+arr[i]
if(x>y):
    d=x-y
else:
    d=y-x
if(d%4==0):
    print('X')
else:
    print('Y')