import math
t=int(input())
for i in range(1,t+1):
    n=int(input())
    sq=n**0.5
    if(int(sq)*sq==n):
        print('True')
    else:
        print('False')