n=100
import math
c=0
k=5
t=1
while t!=0:
    t = math.floor(n/k)
    c+=t
    k = k*5
print(c)
