def modInv(a,m):
    x = -1
    for i in range(1,m):
        if (a*i)%m == 1:
            x = i
            break
    return x
a,m = 4,7
print(modInv(a,m))

