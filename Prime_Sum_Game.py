a,b,c,d=map(int,input().split())
m=n=0
for i in range(a,b+1):
    for j in range(c,d+1):
        s=i+j
        for k in range(2,s):
            if s%k==0:
                break
        else:
            break
    else:
        print("Takahashi")
        exit()
else:
    print("Aoki")