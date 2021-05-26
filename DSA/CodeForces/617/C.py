for _ in range(int(input())):
    n  = int(input())
    s  = input()
    x,y = 0,0
    d = {(0,0):0}
    m = 10000000000
    c1,c2= 0,0
    for i in range(n):
        if s[i] == 'L':
            x-=1
        elif s[i] == 'R':
            x+=1
        elif s[i] == 'U':
            y+=1
        elif s[i] == 'D':
            y-=1
        if (x,y) in d:
            a = d[(x,y)]
            b = i+1
            if b-a<m:
                m = b-a
                c1,c2 = a+1,b
            d[(x,y)] = i+1

        else:
            d[(x,y)] = i+1
    if m == 10000000000:
        print(-1)
    else:
        print(c1,c2)


