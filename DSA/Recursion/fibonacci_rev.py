d={}
def fibi(n):
    if n in d:
        return d[n]
    if n == 1 or n == 0:
        d[n] = 1
        return 1
    p = fibi(n-1)+fibi(n-2)
    d[n] = p
    return p


print(fibi(7))

