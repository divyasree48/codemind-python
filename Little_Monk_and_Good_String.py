s=input()
v='aeiou'
r=c=0
for i in range(len(s)):
    if s[i] in v:
        c+=1
    else:
        r=max(r,c)
        c=0
print(max(r,c))