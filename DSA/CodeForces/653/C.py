for _ in range(int(input())):
    n = int(input())
    s = input()
    st = [s[0]]
    c1,c2=0,0
    for i in range(1,n):
        if len(st)>0 and st[-1] == '(' and s[i] == ')':
            st.pop()
        else:
            st.append(s[i])

    print(len(st)//2)

