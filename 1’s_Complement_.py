n=int(input())
d=''
a=0
while(n):
    r=n%2
    d+=str(r)
    n=n//2
l=d[::-1]
k=''
for i in l:
    if i=='0':
        k+='1'
    else:
        k+='0'
j=int(k)
b=0
while(j):
    r=j%10
    a+=r*(2**b)
    b+=1
    j=j//10
print(a)
