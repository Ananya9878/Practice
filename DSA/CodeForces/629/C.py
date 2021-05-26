for _ in range(int(input())):
    n = int(input())
    x = input()
    a = ''
    b = ''
    flag = True
    for i in range(n):
        if flag:
            if x[i] == '2':
                a+='1'
                b+='1'
            if x[i] == '1':
                a+='1'
                b+='0'
                flag = False
            if x[i] == '0':
                a+='0'
                b+='0'
        else:
            if x[i] == '2':
                a+='0'
                b+='2'
            if x[i] == '1':
                a+='0'
                b+='1'
                flag = False
            if x[i] == '0':
                a+='0'
                b+='0'
    print(a)
    print(b)







