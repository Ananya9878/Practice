from math import log
a=3
r=2
sn=9
n = (log((sn*(r-1)+a)/a)/(log(r)))
if n == int(n):
    n = int(n)
    new_sn = int(a * ((r ** (n-1)) - 1) / (r - 1))
    tn = a * (r ** (n-1))
    x = sn - new_sn
    print(tn - x + 1)

else:
    n = int(n)
    new_sn = int(a*((r**n)-1)/(r-1))
    tn = a*(r**(n))
    x = sn - new_sn
    print(tn-x+1)

