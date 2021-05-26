from functools import reduce

def factors(n):
    l = []
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            l.append(i)
            l.append(n//i)
    return l


for _ in range(int(input())):
    n = int(input())
    l = factors(n)


    flag = False
    flag1 = False
    flag2 = False

    for i in range(len(l)):
        a = l[i]
        b = n//a
        if a!=b:
            flag = True
            break
    if flag:
        # print(a,b,'****')
        p = factors(b)

        l1 = p
        for i in range(len(l1)):
            c = l1[i]
            d = b//c
            if c!=d and d!=a and c!=a:
                flag1 = True
                # print(a,c,d,'%%%%%%%%%%%5')
                break
        if flag1:

            print('YES')
            print(a,c,d)
        else:
            p = factors(a)
            # p.remove(1)
            # s.remove(a)
            l1 = list(p)
            for i in range(len(l1)):
                c = l1[i]
                d = a // c
                if d!=c and b!=d and c!=b:
                    flag2 = True
                    break
            if flag2:
                print('YES')
                print(c,d,b)
            else:
                print('NO')
    else:
        print('NO')






