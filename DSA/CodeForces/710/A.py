for _ in range(int(input())):
    n,m,x = map(int,input().split())

    row = x%n
    column = x/n
    if row == 0:
        row = n
    if column != int(column):
        column = int(column)+1

    res = ((row-1)*m)+column
    print(int(res))

