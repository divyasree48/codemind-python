import math
t=int(input())
for i in range(1,t+1):
    d=0
    s=input()
    for i in s:
        if(i.isnumeric()):
            d+=1;
    if(d==0):
        print('No')
    elif(d!=0):
        print('Yes')