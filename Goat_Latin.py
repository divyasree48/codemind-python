s=input()
n=0
v='aeiouAEIOU'
for i in s.split():
    n+=1
    aaa=[n*'a']
    f1=i[:1]
    if f1 not in v:
        c=i[1:]+f1+'ma'
        c=c+aaa[0]
        print(c,end=' ')
    else:
        c=i+'ma'
        c=c+aaa[0]
        print(c,end=' ')