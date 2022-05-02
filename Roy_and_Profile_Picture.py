l=int(input())
n=int(input())
for i in range(n):
    w,h=map(int,input().split())
    if w<l or h<l:
        print('UPLOAD ANOTHER')
    elif((w>l or h>l) and w!=h):
        print('CROP IT')
    elif(w==h):
        print("ACCEPTED")