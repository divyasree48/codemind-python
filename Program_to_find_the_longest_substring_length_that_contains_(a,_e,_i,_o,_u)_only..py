a=input().lower()
c=0
x=0
v=set('aeiou')
a=list(a)
for i in range(len(a)):
    c=0
    for j in range(i,len(a),1):
        if a[j] in v:
            c+=1
            if x<c:
                x=c
        else:
            break
print(x)
