import math
s=input()
l=list(s.split(' '))
for i in l:
    print(abs(ord(max(i))-ord(min(i))),end=' ')