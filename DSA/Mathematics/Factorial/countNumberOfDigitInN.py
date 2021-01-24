n=1000000
import math
# t = math.factorial(n)
# # print(t)
# p = math.log(t,10)
# p = math.floor(p)+1
# print(p)

c = 0
for i in range(1,n+1):
    c+=math.log(i,10)
print(math.floor(c)+1)

