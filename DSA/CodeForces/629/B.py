for _ in range(int(input())):
    n,k = map(int,input().split())
    l = ['a']*n
    for i in range(n-2,-1,-1):
        p = n-1-i
        if k<=p:
            l[i] = 'b'
            l[n-k] = 'b'
            print(''.join(l))
            break
        k-=p




