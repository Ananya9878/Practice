def display(mat):
    for i in mat:
        print(i)
def create_graph():
    mat = []
    f = open('input1.txt','r')
    v,e = map(int,f.readline().split())
    for i in range(v):
        mat.append([100]*v)
    # print(mat)
    for i in range(e):
        a,b,w = map(int,f.readline().split())
        mat[a][a] = 0
        mat[b][b] = 0
        mat[a][b] = w
        mat[b][a] = w

    display(mat)
    return mat

def floyd_warshall(mat):
    for k in range(len(mat)):
        for i in range(len(mat)):
            for j in range(len(mat)):
                new_cost = mat[i][k]+mat[k][j]
                if new_cost<mat[i][j]:
                    mat[i][j] = new_cost

        display(mat)
        print('***********')
    # d[i][j] = d[i][k]+d[k][j]






if __name__ == '__main__':
    mat=create_graph()
    floyd_warshall(mat)

