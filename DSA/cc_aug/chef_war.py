for i in range(int(input())):
    H,P = map(int,input('enter health and power:').split())
    print(H,P)
    darth_health = H-P
    while P>0:
        P = P // 2
        darth_health = darth_health - P
        if P<=0:
            if darth_health>0:
                print(0)
            else:
                print(1)



