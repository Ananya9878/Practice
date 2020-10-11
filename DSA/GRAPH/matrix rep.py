def create():

    n=int(input('enter no nodes:'))
    m=int(input('number of connections:'))
    # mat = [[0]*n for i in range(n)]
    mat=[]
    for i in range(n):
        mat.append([0]*n)
    # print(mat)
    for i in range(m):
        a,b=map(int,input().split())
        mat[a-1][b-1] = 1
        mat[b-1][a-1] = 1
    return (mat)
'''
k=pop(0)
vistied(k)
print(k)
p = mat[k]
for loop:

'''

def bfs(mat,start):
    queue = [start]
    visited = set()
    while len(queue)>0:
        k = queue.pop(0)
        if k in visited:
            continue
        visited.add(k)
        print(k)
        p = mat[k-1]
        for i in range(len(p)):
            if p[i] == 1:
                queue.append(i+1)

def path(mat,s,e):
    route = [[s]]
    current_route = []
    while len(route)>0:
        k = route.pop()
        q = k[-1]
        conn = mat[q-1]
        flag = True
        for i in range(len(conn)):
            if conn[i] == 1:
                if (i+1) not in k:
                    route.append(k+[i+1])
                    flag = False
        print(route)
        if flag:

            current_route.append(k)
    print(current_route)


def dfs(mat,start):
    stack = [start]
    visited = set()
    while len(stack)>0:
        k = stack.pop()
        if k in visited:
            continue
        visited.add(k)
        print(k,stack,visited)
        q = mat[k-1]
        for i in range(len(q)):
            if q[i] == 1:
                stack.append(i+1)

def add(mat,a,b):
    mat[a-1][b-1] = 1
    mat[b-1][a-1] = 1

def delete(mat,a,b):
    mat[a - 1][b - 1] = 0
    mat[b - 1][a - 1] = 0

'''
stack=[1]
k=1
vistes={1}
print(1,[],{1})
q=[[0, 1, 1, 0, 1, 1]
for...
stack=[2,3,5,6]

'''

def graph():
    g=create()
    print('1 bfs')
    print('2 dfs')
    print('3 add')
    print('4 delete')
    print('5 path')

    while 1:
        option = int(input('enter choice:'))
        if option == 1:

            start = int(input('enter start node'))
            bfs(g,start)
        elif option == 2:
            start=int(input('enter start node:'))
            dfs(g,start)
        elif option == 3:
            a,b = map(int,input('enter 2 values to add').split())
            add(g,a,b)
        elif option == 4:
            a, b = map(int, input('enter 2 values to add').split())
            delete(g,a,b)
        elif option == 5:
            s,e = map(int,input('Enter nodes for path').split())
            path(g,s,e)
        else:
            break
if __name__ == '__main__':
    graph()


