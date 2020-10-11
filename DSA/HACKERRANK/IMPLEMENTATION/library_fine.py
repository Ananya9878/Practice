d1,m1,y1 = list(map(int,input().split()))
d2,m2,y2 = list(map(int,input().split()))
f = 0
if y2 > y1 :
    f = 0

elif y1 == y2 :
    if m1 < m2:
        f = 0

    elif m1 == m2:
        if d1 < d2:
            f = 0

        elif d1 == d2:
            f = 0

        else:
            x = d1 - d2
            f = (x*15)
    else:
        x = m1 - m2
        f = (x*500)


else:
    x = 10000
    f = (x)
print(f)
