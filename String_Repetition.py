s=input()
n=int(input())
l=len(s)
c=0
for i in s:
    if i=='a':
        c+=1
a=n//l
b=n%l
cnt=a*c
for i in range(b):
    if s[i]=='a':
        cnt+=1
print(cnt)