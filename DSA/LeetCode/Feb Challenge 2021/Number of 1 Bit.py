# n = input()
# n = str(bin(n))
# print(n.count('1'))

n = 7
c=0
while n>0:
    if n&1:
        c+=1
    n = n>>1
print(c)




