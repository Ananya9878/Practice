for _ in range(int(input())):
    s = input()
    l = len(s)
    if l & 1:
        print(-1)
    else:
        a = s.count('1')
        b = l-a
        c = abs(a-b)
        if c == l:
            print(-1)
        else:
            print(c//2)



