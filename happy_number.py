def ishappy(res):
    sum=rem=0
    while res>0:
        rem=res%10
        sum=sum+(rem*rem)
        res=res//10
    return sum
n=int(input())
res=n
while res!=1 and res!=4:
    res=ishappy(res)
if res==1:
    print('True')
else:
    print('False')