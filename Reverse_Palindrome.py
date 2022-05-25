def revdigits(num):
    r=0
    while(num>0):
        r=r*10+num%10
        num=num//10
    return r
def pal(n):
    return (revdigits(n)==n)
def rev(n):
    r=0
    while(n<=4294967295):
        r=revdigits(n)
        n=n+r
        if(pal(n)):
            print(n)
            break
n=int(input())
rev(n)