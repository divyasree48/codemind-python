s=input()
l=[]
for i in range(0,len(s)):
    l.append(ord(s[i]))
print(chr(max(l)))