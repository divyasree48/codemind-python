t=int(input())
while(t):
    n=input()
    res=int(n,base=16)
    b=str(bin(res))[2:]
    if len(b)%4!=0:
        k=4-(len(b)%4)
        while(k):
            b='0'+b
            k-=1
    print(b)
    t-=1