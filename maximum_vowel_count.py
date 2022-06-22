def vowelcnt(str):
    l=[]
    vowel=set('aeiouAEIOU')
    for alphabet in str.split():
        cnt=0
        for i in alphabet :
            if i in vowel:
                cnt+=1
            l.append(cnt)
    print(max(l))
str=input()
vowelcnt(str)