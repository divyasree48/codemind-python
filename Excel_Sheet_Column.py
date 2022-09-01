n=int(input())
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=''
while(n):
    r=n%26
    if r==0:
        s+='Z'
        n=(n//26)-1
    else:
        s+=a[r-1]
        n=n//26
k=''
for i in range(len(s)-1,-1,-1):
    k+=s[i]
print(k)