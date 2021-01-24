class Node:
    def __init__(self,info=None):
        self.info = info
        self.children = []

class Graph:
    def __init__(self):
        self.d = {}
        f = open('input.txt','r')
        n = int(f.readline())
        for i in range(n):
            a,b,c = map(int,f.readline().split())
            self.insert_connection(a,b,c)


    def insert_connection(self,parent,child,w1):
        if parent not in self.d:
            self.d[parent] = Node(parent)
        parent_node = self.d[parent]

        if child not in self.d:
            self.d[child] = Node(child)
        child_node = self.d[child]

        parent_node.children.append((child_node,w1))
        child_node.children.append((parent_node,w1))

    def BFS(self,start):
        if start not in self.d:
            return

        z = [(start,0)]
        visited = set()
        while len(z)>0:
            k = z.pop(0)[0]
            for i in self.d[k].children:
                if i in visited:
                    continue
                print(i.info)
                visited.add(i)
                z+=(i.children)


    def DFS(self,start):
        if start not in self.d:
            return
        z = [(start,0)]
        visited = set()
        while len(z)>0:
            p = z.pop()
            k = p[0]
            for i in self.d[k].children:
                if i in visited:
                    continue
                print(i.info)
                visited.add(i)
                z+=(i.children)

    def Path_DFS(self,start,end):
        if start not in self.d and end not in self.d:
            return
        z = [[(start,0)]]
        visited = set()
        while len(z)>0:
            p = z.pop()
            if p[-1][0] == end:
                print(p)
                return p
            k = p[0][0]
            for i in self.d[k].children:
                if i[0] in visited:
                    continue
                #z = z.append((i[0].children,p[0][1]+i[1]))
                z.append(p+[(i[0].info,i[1]+p[-1][-1])])
                visited.add(i[0])

                print(z)

    def mini(self,p):
        m = 0
        for i in range(len(p)):
            # print(p,m)
            if p[i][-1][-1] < p[m][-1][-1]:
                m = i
        k = p.pop(m)
        return k
    '''
    z=[[(1,0)]]
    p = [(1,0),(2,1)]
    k=1...p[0][0]
    z = [(1,0),(2,1)]
    i = (2r,1)'''
    def maxi(self,p):
        m = p[0]
        for i in p:
            if i[-1][-1] > m[-1][-1]:
                m = i
        p.remove(m)
        return m


    def dijkshtra(self,start,end):
        if start not in self.d and end not in self.d:
            return
        z = [[(start,0)]]
        visited = set()
        while len(z)>0:
            p = self.maxi(z)
            k = p[-1][0]
            if k in visited:
                continue
            visited.add(k)
            if k == end:
                print(p)
                break
            for i in self.d[k].children:
                z.append(p+[(i[0].info,i[1]+p[-1][1])])
            # print(z)

    def dijksra_all_path(self,start):
        if start not in self.d:
            return
        z = [[(start,0)]]
        dic = {}
        visited = set()
        while len(z)>0:
            p = self.mini(z)
            k = p[-1][0]
            if k in visited:
                continue
            visited.add(k)
            dic[k] = p
            for i in self.d[k].children:
                z.append(p+[(i[0].info,i[1]+p[-1][1])])
        print(dic)

G = Graph()
print('1 create')
print('2 dfs ')
print('3 bfs')
print('4 path')
print('5 dijshtra')
print('6 dijkshtra_all_path')
while 1:
    option = int(input('enter option'))
    if option == 1:
        p,c,w = map(int, input('enter 3 nodes to connect:').split())
        G.insert_connection(p, c,w)
    elif option == 2:
        G.DFS(int(input('enter start')))
    elif option == 3:
        G.BFS(int(input('enter start')))
    elif option == 4:
        s,e = map(int,input('enter 2 values').split())
        G.Path_DFS(s,e)
    elif option == 5:
        s, e = map(int, input('enter 2 values').split())
        G.dijkshtra(s, e)
    elif option == 6:
        G.dijkshtra_all_path(int(input('enter start node:')))





