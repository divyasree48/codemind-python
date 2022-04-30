t=int(input())
for i in range(1,t+1):
    n=int(input())
    rev=0
    temp=n
    while(n):
        r=n%10
        n=n//10
        rev=rev*10+r
    if(temp==rev):
        print('True')
    else:
        print('False')