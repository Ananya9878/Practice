for _ in range(int(input())):
    n = int(input())
    t = 2
    while 1:
        x = n / ((2 ** t) - 1)
        if x == int(x):
            print(int(x))
            break
        else:
            t+=1







