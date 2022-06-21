s=input()
s=s.lower()
str=""
for i in s:
    str=i+str
if str==s:
    print('True')
else:
    print('False')