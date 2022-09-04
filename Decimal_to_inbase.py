a=int(input())
b=int(input())
arr=[]
while a>0:
    r=a%b
    arr.append(r)
    a//=b
c=m=0
for i in range(len(arr)):
    c=0
    for j in range(i,len(arr)):
        if arr[j]==0:
            c+=1
            if m<c:
                m=c
        else:
            break
if m==0:
    print(-1)
else:
    print(m)