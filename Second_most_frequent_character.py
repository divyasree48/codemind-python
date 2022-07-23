s=input()
charcnt=256
cnt=[0]*charcnt
for i in range(len(s)):
    cnt[ord(s[i])]+=1

o,t=0,0
for i in range(charcnt):
    if cnt[i]>cnt[o]:
        t=o
        o=i
    elif cnt[i]>cnt[t] and cnt[i]!=cnt[o]:
        t=i
if chr(t)!=NULL:
    print(chr(t))
else:
    print(-1)