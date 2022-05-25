t=int(input())
for i in range(t):
    s=input().lower()
    if "".join(reversed(s))==s:
        if len(s)%2==0:
            print("YES EVEN")
        elif len(s)%2!=0:
            print("YES ODD")
    else:
        print("NO")