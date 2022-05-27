n=int(input())
arr=list(map(int,input().split()))
hcf=arr[0]
j=1
while(j<n):
    if(arr[j]%hcf==0):
        j+=1
    else:
        hcf=arr[j]%hcf
print(hcf)
        