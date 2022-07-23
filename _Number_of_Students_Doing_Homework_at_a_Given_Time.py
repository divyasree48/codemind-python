n1=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n1):
    for j in range(i,i+1):
        if (arr1[i]<=k and arr2[j]>=k):
            c+=1
        else:
            continue
print(c)
