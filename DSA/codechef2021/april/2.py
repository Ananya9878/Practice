n = int(input())
arr = list(map(int,input().split()))
n1 = int(input())
q = list(map(int,input().split()))
s = sum(arr)
mod = 10**9+7
for i in range(n1):
    p = pow(2,i+1,mod)
    print((s*p)%mod)
