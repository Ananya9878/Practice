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
    # queue = [(start,0)]
    queue = [start]
    visited=set()
    while len(queue)>0:
        k = queue.pop(0)
        if k in visited:
            continue
        visited.add(k)
        print(k,queue,visited)
        conn = l[k-1]
        # queue+=l[k-1]
        for i in conn:
            queue.append(i[0])



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
        conn = l[k-1]
        for i in conn:
            stack.append(i[0])

def check(v,k):
    for i in k:
        # print(i)
        if i[0] == v:
            return False
    return True
            # print('y')
'''
l=[[(2,1)]
[(1,1),(3,1)]
[(2,1)]]
root = [[(1,0)]]
k = [(1,0)]
q = 1
conn =[(2,1)]
i=(2,1)
route =[[(1,0)]+[(2,1)]]
route =[[(1,0),(2,1)]]
k =[(1,0),(2,1)]
q = 2
conn = [(1,1),(3,1)]
i = (3,1)
route = [(1,0),(2,1)] + [(3,1+1)]
==[[(1,0),(2,1),(3,2)]] 
  
'''
def path(l,s,e):
    route = [[(s,0)]]
    complete_path = []
    while len(route)>0:
        k = route.pop()
        q = k[-1][0]
        conn = l[q-1]
        flag = True
        for i in conn:
            if check(i[0],k):
                route.append(k+[(i[0],k[-1][1]+i[1])])
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
        a,b,c = map(int,input().split())
        l[a-1].append((b,c))
        l[b-1].append((a,c))
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



















