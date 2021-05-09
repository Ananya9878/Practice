# from functools import reduce
# def fun(n):
#     return str(int(n) + 1)
# for _ in range(int(input())):
#     a,b = map(int,input().split())
#     t = str(a)
#
#     mod = (10**9)+7
#     while b!=0:
#         h = list(map(fun, str(t)))
#         p = ''.join(h)
#         t = p
#         b-=1
#     v = len(t)%mod
#     print(v)
MOD = 10 ** 9 + 7
dp = [0 for _ in range(202020)]
for i in range(9):
    dp[i] = 1
dp[9] = 2
for i in range(10, 202020):
    dp[i] = (dp[i - 9] + dp[i - 10]) % MOD

t = ip()
while t:
    ans = 0
    t -= 1
    n, k = mip()

    while n:
        if k + n % 10 < 10:
            ans += 1
        else:
            ans += dp[k + n % 10 - 1]
        n //= 10

    print(ans % MOD)