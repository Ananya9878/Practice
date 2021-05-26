for _ in range(int(input())):
    n,k = map(int,input().split())
    t = n//k
    r = n%k
    p = k//2
    ans = (t*k)+min(r,p)
    print(ans)

