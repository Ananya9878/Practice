for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    c0 = 0
    c1 = 0
    i=0
    m = ''
    flag = True
    while i<n:
        if s[i] == '1':
            c1+=1
            # i+=1
        else:
            if k>=c1:
                k = k-c1
                c0+=1
            else:
                m = '1'*(c1-k)+'0'+'1'*k
                flag=False
                break
        i+=1
    if flag:
        p = '0'*c0+'1'*c1
    else:
        p = '0'*c0+m+s[i+1:]
    print(p)









