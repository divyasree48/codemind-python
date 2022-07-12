n=int(input())
arr=list(map(int,input().split()))
s1=list(set(arr))
c=s=0
for i in s1:
    if arr.count(i)==i:
        c+=1
        s+=i
if(c>0):
    print("%.2f"%(s/c))
else:
    print(-1)