for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
        continue
    p = len(bin(n)[2:])
    m = '1'*(p-1)
    print(int(m,2))