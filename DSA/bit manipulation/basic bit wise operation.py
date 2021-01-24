#and operation
a = 5
b = 6
print(a^b)
print(a&b)
print(a|b)
print(~6,"*",)
# shift operation
#left shift << multiply
print(a<<2)
#right shift >> divide(integral division)
print(a>>1)
#power
print((1<<2))
# set bit
c = 23
k = 3
print((c>>(k-1))&1)
#count total 1 in binary
n = 23
c = 0
while n>0:
    if n&1 == 1:
        c+=1
    n=n>>1
print(c)

# toggle
n = 23
k = 4
p = 1<<(k-1)
print(n^p)
# set bit
n = 21
k = 5
p = 1<<(k-1)
print(n|p)
# unset bit
n = 21
k = 5
p = 1<<(k-1)
p = (~p)
print(n&p)













