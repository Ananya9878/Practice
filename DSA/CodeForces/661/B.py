for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    m1,m2 = min(a),min(b)
    res = 0
    for i in range(n):
        p = a[i]-m1
        q = b[i]-m2
        res+=max(p,q)
    print(res)