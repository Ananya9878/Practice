for _ in range(int(input())):
    n = int(input())
    mat = []
    t = []
    for i in range(n):
        l = list(input())
        if len(t)<3:
            for j in range(n):
                if l[j] == '*':
                    k = (i,j)
                    t.append((k))
        mat.append(l)
    a,b = t[0]
    c,d = t[1]
    if d==b:
        if d!=0:
            mat[a][0] = '*'
            mat[c][0] = "*"
        else:
            mat[a][n-1] = '*'
            mat[c][n-1] = '*'
    elif a==c:
        if a!=0:
            mat[0][b] = '*'
            mat[0][d] = "*"
        else:
            mat[n - 1][b] = '*'
            mat[n - 1][d] = '*'

    else:
        mat[a][d] = '*'
        mat[c][b] = '*'


    for i in mat:
        p = ''.join(i)
        print(p)
  