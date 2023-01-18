n=int(input())
a=n%100
b=str(a)
if(len(b)<2):
    b='0'+b
print(b)