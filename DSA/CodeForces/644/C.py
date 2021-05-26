for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    p  = set(l)
    d = {0: 0, 1: 0}
    for i in range(n):
        if l[i]%2==0:
            d[0]+=1
        else:
            d[1]+=1

    if d[0]%2==0:
        print('YES')
    else:
        if len(set(l)) == 1:
            print('YES')
            continue
        for i in l:
            if i + 1 in p:
                print('YES')
                break
        else:
            print('NO')


    #
    # else:
    #     l.sort()
    #
    #
    #     for i in range(n - 1):
    #         if abs(l[i] - l[i + 1]) == 1:
    #             d[1] += 1
    #         # if d[0]>=2 or d[1]>=2:
    #         #     break
    #     print(d,d[1],d[0])
    #     if d[1]>=2 or d[0]>=2:
    #         print('YES')
    #     else:
    #         print('NO')


