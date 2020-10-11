for i in range(int(input())):
    c,r = map(int,input().split())
    d = c//9
    if c%9 != 0:
        d+=1

    d2 = r//9
    if r%9 !=0:
        d2+=1

    if d>d2:
        print(1,d2)
    elif d == d2:
        print(1,d2)
    else:
        print(0,d)






