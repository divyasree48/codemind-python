d=0
s=input()
for i in s:
    if(i.isnumeric()):
        d+=1;
if(d!=0):
    print('Contains %d digit'%d)
else:
    print("Doesn't contain digit")