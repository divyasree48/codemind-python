n=int(input())
l=list(map(int,input().split()))
s=sorted(l)
#if n%2==0:
 #   print((s[n//2]+s[(n//2)+1])//2)
#else:
print(s[(n//2)])