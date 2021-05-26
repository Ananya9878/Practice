for _ in range(int(input())):
    n = int(input())
    res = 0
    if n%2 == 0:
        res = (n//2)-1

    else:
        res = n//2

    print(res)
        