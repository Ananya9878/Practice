# 3
# [[1 2],[1 3],[2 3]]
# [[2,3] [1,3] [1,2]]
# n=3
# [[2],[],[]]
# i=0 a,b 1 2
# a=1 b=2
# l[1]...2.....
#l= [[2],[],[]]
# i=1
# a,b=1,3
# l[0]...3
# l= [[2,3],[],[]]
def bfs(l,start):
    queue = [start]
    visited=set()
    while len(queue)>0:
        k = queue.pop(0)
        if k in visited:
            continue
        visited.add(k)
        print(k,queue,visited)
        queue+=l[k-1]
'''
start=1

[1]
[1,2], [1,5], [1,3]
[1,2,5], [1, 2, 4],[1,5,7],[1,5,2],[1,3,6]
[1,2,5,7],[1,2,4,7],[1,5,7,6],[1,5,7,4],[1,5,2,4],[1,3,6,7]
[1,2,5,7,6],[1,2,5,7,4],[1,2,4,7,6],[1,2,4,7,5],[1,5,7,6,3],[1,5,7,4,2],
...[1,5,2,4,7],[1,3,6,7,5],[1,3,6,7,4]


'''

def dfs(l,start):
    stack = [start]
    visited=set()
    while len(stack)>0:
        k = stack.pop()
        if k in visited:
            continue
        visited.add(k)
        print(k, stack, visited)
        stack+=l[k - 1]

def path(l,s,e):
    route = [[s]]
    complete_path = []
    while len(route)>0:
        k = route.pop()
        q = k[-1]
        conn = l[q-1]
        flag = True
        for i in conn:
            if i not in k:
                route.append(k+[i])
                flag = False
        print(route)

        if flag:
            complete_path.append(k)

    print(complete_path)





def create_graph():
    n=int(input('no of nodes:'))
    l=[[] for i in range(n)]
    k = int(input('enter no of connections:'))
    for i in range(k):
        a,b = map(int,input().split())
        l[a-1].append(b)
        l[b-1].append(a)
    return l

def display(l):
#     for i in l:
#         print(i)
    print('\n'.join(map(str,l)))

def add_conn(l,a,b):
    l[a - 1].append(b)
    l[b - 1].append(a)


def graph():
    g=create_graph()
    print('1 bfs')
    print('2 dfs')
    print('3 add connection')
    print('4 display')
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
            a,b=map(int,input('enter 2 element to add').split())
            add_conn(g,a,b)
            print(g)
        elif option == 4:
            display(g)
        elif option == 5:
            s,e = map(int,input('enter staet and end node').split())
            path(g,s,e)
        else:
            break
if __name__ == '__main__':
    graph()



















