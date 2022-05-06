s=input()
j=0
k=0
for i in s:
    if(i=='z'):
        j+=1
    else:
        k+=1
if(2*j==k):
    print('Yes')
else:
    print('No')