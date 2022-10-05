s=input().split(' ')
k=sorted(s)
k.sort(key=len)
print(*k)
