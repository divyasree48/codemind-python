def isprime(n):
    v=0
    for i in range(1,n+1):
        if n%i==0:
            v+=1
    if v==2:
        return 1
    else:
        return 0
n=int(input())
if isprime(n):
    c=0
    rev=0
    while(n):
        d=n%10
        rev=(rev*10)+d
        n=n//10
    if (isprime(rev)):
         c+=1
    if c!=0:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")