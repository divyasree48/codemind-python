n=int(input())
w=[]
for j in range(n):
    a=int(input())
    w.append(a)
t=int(input())
a=0
for i in range(n): 
    if(w[i]>t):
        a=a+2
    else:
        a=a+1
print(a)
    
    