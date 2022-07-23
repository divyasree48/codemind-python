def fun(k):
    if k=='I':
        return 1
    if k=='V':
        return 5
    if k=='X':
        return 10
    if k=='L':
        return 50
    if k=='C':
        return 100
    if k=='D':
        return 500
    if k=='M':
        return 1000
    return -1
def roman(s):
    res=i=0
    while(i<len(s)):
        s1=fun(s[i])
        if(i+1<len(s)):
            s2=fun(s[i+1])
            if s1>=s2:
                res=res+s1
                i=i+1
            else:
                res=res+s2-s1
                i=i+2
        else:
            res+=s1
            i+=1
    return res
s=input()
print(roman(s))