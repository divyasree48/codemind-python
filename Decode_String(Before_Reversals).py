t=int(input())
while(t):
    n,k=map(int,input().split())
    s=input().lower()
    
    for i in range(k-1,-1,-1):
        s1=''
        for j in range(i+1,len(s),1):
            s1+=s[j]
      
        s=s[i::-1]+s1
        if i==0:
            print(s)
    t-=1
        
    