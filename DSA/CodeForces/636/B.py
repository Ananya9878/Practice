for _ in range(int(input())):
    n = int(input())
    l = [i*2 for i in range(1,n//2+1)]
    l2 = []
    for i in range(len(l)-1):
        l2.append(l[i]-1)
    c = l[-1]+len(l)-1
    if c&1:
        l2.append(c)
    t = l + l2

    if sum(l) == sum(l2):
        print('YES')
        print(*t)
    else:
        print('NO')
