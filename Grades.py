a,b,c,d,e=map(int,input().split())
f=(a+b+c+d+e)/5
if(f>=90):
    print('Grade A')
elif f>=80:
    print("Grade B")
elif f>=70:
    print("Grade C")
elif f>=60:
    print("Grade D")
elif f>=40:
    print("Grade E")
else:
    print("Grade F")