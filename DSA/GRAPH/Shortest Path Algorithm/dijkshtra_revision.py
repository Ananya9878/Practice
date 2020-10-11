class Node:
    def __init__(self, info=None):
        self.info = info
        self.children = []


class Graph:
    def __init__(self):
        self.d = {}
        n = int(input('no of connection:'))
        f = open('input.txt','r')
        for i in range(n):
            a,b,c = map(int,f.readline().split())
            self.insert_connection(a,b,c)

    def insert_connection(self, p, c,w):
        if p not in self.d:
            self.d[p] = Node(p)
        p_node = self.d[p]

        if c not in self.d:
            self.d[c] = Node(c)
        c_node = self.d[c]
        p_node.children.append((c_node,w))
        c_node.children.append((p_node,w))

    def mini(self,p):
        k = 0
        for i in range(len(p)):
            if p[i][-1][-1] < p[k][-1][-1]:
                k = i
        return p.pop(k)

    def dijkshtra(self,start,end):
        if start not in self.d and end not in self.d:
            return
        z = [[(start,0)]]
        visited = set()
        while len(z)>0:
            q = self.mini(z)
            k = q[-1][0]
            if k == end:
                print(q)
                break
            if k in visited:
                continue
            visited.add(k)
            for i in self.d[k].children:
                z.append(q+[(i[0].info,i[1]+q[-1][-1])])

    def dijkshtra_all_path(self,start):
        if start not in self.d:
            return
        z = [[(start,0)]]
        visited = set()
        path = {}
        while len(z)>0:
            q = self.mini(z)
            k = q[-1][0]
            if k in visited:
                continue
            visited.add(k)
            path[k] = q
            for i in self.d[k].children:
                z.append(q+[(i[0].info,i[1]+q[-1][-1])])
        print(path)







G = Graph()
print('1 create')
print('2 dijkshtra algo ')
print('3 dijkshtra_all')
while 1:
    option = int(input('enter option'))
    if option == 2:
        p, e= map(int, input('enter 2 nodes to connect:').split())
        G.dijkshtra(p,e)
    elif option == 3:
        s = int(input('enter start node:'))
        G.dijkshtra_all_path(s)
    else:
        break






