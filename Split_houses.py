n=int(input())
s=input()
t=s.replace('.','B')
if 'HH' in s:
    print('NO')
else:
    print('YES')
    print(t)