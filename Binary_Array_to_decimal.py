n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in l[::-1]:
    d+=(2**c)*i
    c+=1
print(d)