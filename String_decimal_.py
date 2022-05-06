t=int(input())
j=1
while(j<=t):
    s=input()
    l=len(s)
    c=0
    for i in s:
        if(i>='0' and i<='9'):
            c+=1
    if(c==l):
        print('True')
    else:
        print('False')
    j+=1