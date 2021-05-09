def fun(a,b,x,y,n):
    k = a-x
    if n>=k:
        a = x
        n = n-k
    else:
        a = a-n
        n = 0

    k = b - y
    if n >= k:
        b = y
        n = n - k
    else:
        b = b - n
        n = 0
    return a*b

def fun1(a,b,x,y,n):
    k = b - y
    if n >= k:
        b = y
        n = n - k
    else:
        b = b - n
        n = 0
    k = a-x
    if n>=k:
        a = x
        n = n-k
    else:
        a = a-n
        n = 0


    return a*b

for i in range(int(input())):
    a,b,x,y,n = map(int,input().split())
    p = fun1(a,b,x,y,n)
    q = fun(a,b,x,y,n)
    print(min(p,q))






