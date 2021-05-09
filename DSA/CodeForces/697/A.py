import math

for _ in range(int(input())):
    n = int(input())
    a = bin(n)[2:]
    p = a.count('1')
    if p == 1:
        print('NO')
    else:
        print('YES')
