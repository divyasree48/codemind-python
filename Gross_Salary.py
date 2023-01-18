a=int(input())
if(a<=10000):
    b=(80*a)/100
    c=(20*a)/100
elif a<=20000:
    b=(90*a)/100
    c=(25*a)/100
else:
    b=(95*a)/100
    c=(30*a)/100
d=str(a+b+c)
e,f=d.split('.')
if(len(f)<2):
    f=f+'0'
print(e,end='.')
print(f)