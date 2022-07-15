s1=input()
l=list(s1.split(' '))
s=''
for i in l:
    s+=i
print(min(s),s.count(min(s)),max(s),s.count(max(s)))