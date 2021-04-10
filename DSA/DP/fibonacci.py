def fab(n,d):
    # if n in d:
    #     return d[n]
    if d[n] != -1:
        return d[n]
    print('function called for n=',n)
    if n==0:
        return 0
    if n==1:
        return 1

    r = fab(n-1,d)+fab(n-2,d)
    d[n] = r
    return r
# d = {}
n = 8
d = [-1]*(n+1)
print(fab(n,d))

# 0 1 1 2 3 5 8 13

