n=int(input())
temp=n
rev=0
sum=0
while(n):
    r=n%10
    n=n//10
    rev=rev*10+r
while(rev):
    k=rev%10
    rev=rev//10
    f=1
    for i in range(1,k+1):
        f=f*i
    sum=sum+f
a=temp
if(sum==temp):
    print('The number', a ,'is a strong number')
else:
     print('The number', a ,'is not a strong number')    
    
    