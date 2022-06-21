def iso(s):
    return (len(s)==len(set(s.lower())))
s=input()
if(iso(s)==True):
    print('True')
else:
    print('False')
    