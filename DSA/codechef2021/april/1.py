for _ in range(int(input())):
    n = int(input())
    s = input()
    c1,c0 = 0,0
    flag = False
    for i in range(n):
        if s[i] == '0':
            c0+=1
        else:
            c1+=1
        if c1==c0:
            flag = True
            break
    if flag:
        print('YES')
    else:
        print('NO')










