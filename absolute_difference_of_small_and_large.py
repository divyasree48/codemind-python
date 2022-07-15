s=input()
l=list(s.split(' '))
for i in l:
    print(ord(max(i))-ord(min(i)),end=' ')