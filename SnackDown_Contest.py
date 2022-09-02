t=int(input())
for a in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    l=[]
    m=[]
    for i in range(1,len(p)):
        if p[i] not in m:
            m.append(p[i])
    for i in range(1,len(q)):
        if q[i] not in m:
            m.append(q[i])
    if len(m)>=n:
        print('YES')
    else:
        print('NO')