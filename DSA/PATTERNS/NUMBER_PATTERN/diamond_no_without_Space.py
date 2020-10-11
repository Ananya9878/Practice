n=6
for i in range(n):
    print(' '*(n-i-1),end='')
    print((str(i+1)*(2*i+1)))
for i in range(n-1,0,-1):
    print(' ' *(n - i), end='')
    print((str(i) * (2*i-1)))