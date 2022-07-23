def vow(c):
    v='aeiouAEIOU'
    if c in v:
        return True
    return False
def revvow(s):
    j=0
    vowel=[0]*len(s)
    s=list(s)
    for i in range(len(s)):
        if vow(s[i]):
            vowel[j]=s[i]
            j+=1
    for i in range(len(s)):
        if vow(s[i]):
            j-=1
            s[i]=vowel[j]
    return ''.join(s)
s=input()
print(revvow(s))