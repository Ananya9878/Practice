for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    m = 1000000000
    for i in range(n-1):
        p = abs(l[i]-l[i+1])
        if p<m:
            m = p
    print(m)
