s=input()
l=list(s.split(' '))
max=-999
for i in l:
    if(len(i)>max):
        max=len(i)
print(max)