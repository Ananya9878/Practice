n,c,m = map(int,input().split())
x = n//c
k = x
while k >= m:
    q = k//m
    x+=q
    q+=(k%m)
    k = q
print(x)
