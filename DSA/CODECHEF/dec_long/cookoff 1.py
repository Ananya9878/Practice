for _ in range(int(input())):
    n = int(input())
    s = input()
    l = 120-n
    a = s.count('0')
    b = s.count('1')


    if b+l>=90:
        print('YES')
    else:
        print('NO')