n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)

i=j=0

while(i<len(a)):
    print(a[i],end=' ')
    
    i+=1
while(j<len(b)):
    
    print(b[j],end=' ')
    
    j+=1
