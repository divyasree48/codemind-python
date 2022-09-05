def rev(s):
    if len(s)==1:
        return s
    s1=""
    for i in range(len(s)-1,-1,-1):
        s1+=s[i]
    return s1
s=input()
st=""
a=0
for i in range(len(s)):
    s2=""
    for j in range(i,len(s)):
        s2+=s[j]
        if s2==rev(s2):
            if s2 in s:
                if len(s2)>a:
                    st=s2
                    a=len(st)
print(st) 