for _ in range(int(input())):
    n = int(input())
    cost = 0
    while n>=10:
        # print(n)
        p = n//10
        q  = n%10
        cost+=(p*10)
        n = p+q

    print(cost+n)
