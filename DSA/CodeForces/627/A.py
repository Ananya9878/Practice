for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    flag = True
    m = max(arr)
    for i in range(n):
        if (m-arr[i])&1:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')



