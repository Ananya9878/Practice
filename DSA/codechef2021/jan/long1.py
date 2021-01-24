for _ in range(int(input())):
    n,k,d = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr+=[0]
    s = sum(arr)
    if s<k:
        print(0)
    else:
        a = s%k
        b = s//k
        if b<=d:
            print(b)
        else:
            print(d)

