s=input()
l=list(s.lower())
l1=[]
for i in l:
    if i==' ':
        continue
    if l.count(i)==1:
        l1.append(i)
'''print(l1)'''
if(len(l1)==0):
    print(-1)
else:
    print(l1[0])