for _ in range(int(input())):
    a,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    s = sum (arr)
    a = s%k
    if a == 0:
        print(0)
    else:
        print(1)

