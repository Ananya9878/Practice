for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
# n=5
# l = [1,2,2,1,3]
    d = {}
    if len(set(l)) == 1:
        print('NO')
    else:
        print('YES')
        for i in range(n):
            if l[i] not in d:
                d[l[i]] = [i+1]
            else:
                d[l[i]].append(i+1)
        k = list(d.keys())
        a = d.pop(k[0])

        for i in d:
            p = d[i]
            for j in p:
                print(a[0],j)
        b = d.pop(k[1])
        for i in range(1,len(a)):
            print(b[0],a[i])








