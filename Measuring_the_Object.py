w,x,y,z=map(int,input().split())
#print(w,x,y,z)
k=0
if x==w or y==w or z==w:
    k=1
elif x+y==w or x+z==w or y+z==w:
    k=1
elif x+y+z==w:
    k=1
if(k==1):
    print('YES')
else:
    print('NO')