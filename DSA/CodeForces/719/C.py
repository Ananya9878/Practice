for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(-1)
        continue
    if n == 3:
        print(2,9,7)
        print(4,6,3)
        print(1,8,5)
        continue
    mat = [[-1]*n for i in range(n)]
    c = 1
    for i in range(n):
        for j in range(0,n,2):
            mat[i][j] = c
            c+=1

    for i in range(n):
        for j in range(1,n,2):
            mat[i][j] = c
            c+=1
    for i in mat:
        print(*i)
