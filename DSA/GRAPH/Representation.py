def create_list():
    n = int(input('Enter number of nodes'))
    l = [[] for i in range(n)]
    conn = int(input('enter no of connections'))
    for i in range(conn):
        a,b = map(int,input().split())
        l[a-1].append(b)
        l[b-1].append(a)

    return l

# print(create_list())


def create_matrix():
    n = int(input('enter no of nodes'))
    m = int(input('enter no of connections'))
    mat=[]
    for i in range(n):
        mat.append([0]*n)
    for i in range(m):
        a,b = map(int,input().split())
        mat[a-1][b-1]=1
        mat[b-1][a-1]=1
    print(mat)
print(create_matrix())
