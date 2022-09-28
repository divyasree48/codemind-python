n=int(input())
emails=[]
for i in range(n):
    k=input()
    emails.append(k)
st = set()
for e in emails:
    name, domain = e.split('@')
    #print(name)
    #print(domain)
    local = name.split('+')[0].replace('.', '')
    #print(local)
    st.add(local + '@' + domain)    
print(len(st))