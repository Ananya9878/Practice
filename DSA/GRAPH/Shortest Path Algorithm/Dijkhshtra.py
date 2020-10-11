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
            a,b,c,d,e = map(int,f.readline().split())
            self.insert_connection(a,b,c,d,e)

    def insert_connection(self, p, c,w1,w2,w3):
        if p not in self.d:
            self.d[p] = Node(p)
        p_node = self.d[p]

        if c not in self.d:
            self.d[c] = Node(c)
        c_node = self.d[c]
        p_node.children.append((c_node,w1,w2,w3))
        c_node.children.append((p_node,w1,w2,w3))

    def min_weight(self,p):
        min_index = 0
        for i in range(len(p)):
            w = p[i][-1]
            if w[1]+w[2]+w[3] < p[min_index][-1][1]+p[min_index][-1][2]+p[min_index][-1][2]:
                min_index = i
        return p.pop(min_index)

    def max_weight(self,p):
        min_index = 0
        for i in range(len(p)):
            if p[i][-1][1] > p[min_index][-1][1]:
                min_index = i
        return p.pop(min_index)

    def Dijkstra(self,start,end):
        if start not in self.d and end not in self.d:
            return
        p = [[(start,0,0,0)]]
        visited = set()

        '''
        [[(1,0)]]
        []
        p=[[(1,0),(2,1)],[(1,0),(3,1)]]
        k=[(1,0),(2,1)]
        '''
        while len(p)>0:
            k = self.max_weight(p)
            q = k[-1]
            if q[0] in visited:
                continue
            if q[0] == end:
                print(k)
                break
            # print(k)
            visited.add(q[0])
            for i in self.d[q[0]].children:
                p.append(k+[(i[0].info,i[1]+q[1],i[2]+q[2],i[3]+q[3])])
            # print(p)

G = Graph()
print('1 create')
print('2 dijkshtra algo ')
while 1:
    option = int(input('enter option'))
    if option == 1:
        p,c,w = map(int, input('enter 2 nodes to connect:').split())
        G.insert_connection(p, c,w)
    elif option == 2:
        p, e= map(int, input('enter 2 nodes to connect:').split())
        G.Dijkstra(p,e)
    else:
        break
