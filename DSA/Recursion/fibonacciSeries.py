# a = [0]*10
# a[0]=1
# a[1]=1
# i=2
# while i < 10:
#     a[i] = (a[i-2]+a[i-1])
#     i+=1
# print(a)
#
#
# a=1
# b=1
# i=2
# while i < 10:
#     t = a+b
#     a = b
#     b = t
#
#     i+=1
#     print(t)
# def fib(i,n,a,b):
#     if n == 0 or n == 1:
#         return 1
#     if i==n:
#         return b
#     return fib(i+1,n,b,a+b)
# print(fib(1,20,1,1))
d = {}
def fib1(n):
    if n in d:
        return d[n]
    print(n)
    if n == 1 or n == 0:
        d[n] = 1
        return 1
    k = fib1(n-1) + fib1(n-2)
    d[n] = k
    return k

print(fib1(5))



















