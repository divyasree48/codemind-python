n=int(input())
c=0
i=2
j=0
while(1):
    if c>n:
        break
    if c==0:
        print(0,end=' ')
    else:
        if c%2==0:
            print(i,end=' ')
            i+=2
        else:
            print(j,end=' ')
            j+=1
    c+=1