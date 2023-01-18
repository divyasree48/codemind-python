n=int(input())

if(n<=199):
    a=1.20;
elif(n>=200 and n<400):
    a=1.50;
elif(n>=400 and n<600):
    a=1.80;
else:
    a=2.00;

   
if(n*a>=400):
    b=(15*n*a)/100;
else:
    b=100;

z=str((n*a)+b)
x,y=z.split('.')
if(len(y)<2):
    y=y+'0'
print(x,end='.')
print(y)
    
