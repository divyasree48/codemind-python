s=input()
k=s.split()
p=[]
for i in k:
    p.append(i[::-1])
print(' '.join(p))