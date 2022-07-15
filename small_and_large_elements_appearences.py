s1=input()
s=''
for i in s1.split(' '):
    s=s+i
        
print(min(s),s1.count(min(s)),max(s),s1.count(max(s)))