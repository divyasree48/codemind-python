s=input()
k=sorted(s)
l=''
st='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'
for i in k:
    if i.isalpha():
        l+=i
j=0
for i in s:
    if i.isalpha():
        st+=l[j]
        j+=1
    else:
        st+=i
print(st)
    