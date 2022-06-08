r=int(input())
arr=[list(map(int,input().split()))for i in range(r)]
s=0
s1=0
for i in range(r):
    for j in range(r):
        if(i==j):
            s=s+arr[i][j]
for i in range(r):
    for j in range(r):
        if(i==r-j-1):
            s1+=arr[i][j]
a='Principal Diagonal:'
b='Secondary Diagonal:'
c=s
d=s1
print('{0}{1}'.format(a,c))
print('{0}{1}'.format(b,d))