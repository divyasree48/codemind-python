t=int(input())
while(t):
    s=input()
    st=[]
    k=0
    for i in s:
        if i in '{[(':
            st.append(i)
        else:
            if len(st)==0:
                k=1
                break
            else:
                if i==')' and st[-1]=='(':
                    st.pop()
                elif i==']' and st[-1]=='[':
                    st.pop()
                elif i=='}' and st[-1]=='{':
                    st.pop()
                else:
                    k=1
                    break
    if k==1:
        print('False')
    else:
        print('True')