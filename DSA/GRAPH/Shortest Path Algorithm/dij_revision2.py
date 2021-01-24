class Node:
    def __init__(self,info=None):
        self.info = info
        self.children = []

class Graph:
    def __init__(self):
        self.d={}
        f = open('input.txt','r')
        n,c = map(int,f.readline().split())
        for i in range(c):
            p,c,w = map(int,f.readline().split())
            self.insert(p,c,w)


    def insert(self,p,c,w):
        if p not in self.d:
            self.d[p] = Node(p)
        p_node = self.d[p]

        if c not in self.d:
            self.d[c] = Node(c)
        c_node = self.d[c]

        p_node.children.append((c_node,w))
        c_node.children.append((p_node,w))

    def Dfs(self,start,end):
        root = self.d[start]
        z=[(root,0)]
        visited = set()
        while len(z)>0:
            p = z.pop()
            if p[0] in visited:
                continue
            print(p[0].info,p[1])
            if p[0].info == end:
                break
            for i in p[0].children:
                if i[0] not in visited:
                    z.append((i[0],p[1]+i[1]))

            visited.add(p[0])


    def Bfs(self,start,end):
        root = self.d[start]
        visited = set()
        z = [(root,0)]
        while len(z)>0:
            p = z.pop(0)
            if p[0] in visited:
                continue
            print(p[0].info,p[1])
            if p[0].info == end:
                break

            for i in p[0].children:
                if i[0] not in visited:
                    z.append((i[0],p[1]+i[1]))
            visited.add(p[0])


    def mini(self,k):
        m = k[0]
        for i in k:
            if m[1] > i[1]:
                m = i
        return m

    def dijkstra(self,start,end):
        root = self.d[start]
        z = [(root,0)]
        visited = set()
        while len(z)>0:
            p = self.mini(z)
            z.remove(p)

            if p[0] in visited:
                continue
            print(p[0].info,p[1])
            if p[0].info == end:
                break

            for i in p[0].children:
                if i[0] not in visited:
                    z.append((i[0],i[1]+p[1]))
            visited.add(p[0])

    def minimum(self,p):
        # print(p)
        mini = p[0]
        for i in p:
            if i[-1][-1] < mini[-1][-1]:
                mini = i
        return mini


    def dijkstra_shortest_path(self,start,end):
        t =[(start,0)]
        s = self.d[t[-1][0]]
        visited = set()
        while len(t)>0:
            p = self.minimum(t)
            t.remove(p)
            if p[0] in visited:
                continue
            print(p)
            if p[0] == end:
                break
            for i in self.d[p[0]].children:
                if i[0].info not in visited:
                    t.append((i[0].info,p[1]+i[1]))
            visited.add(p[0])

    def path(self,start,end):
        s=[[(start,0)]]
        visited = set()
        dic = {}
        while len(s)>0:
            p = self.minimum(s)
            s.remove(p)
            t = p[-1]
            a = t[0]
            if a not in dic:
                dic[a] = p
            if a == end:
                print('shortest path',p)
                # break
            if a in visited:
                continue
            visited.add(a)
            print(p)
            for i in self.d[a].children:
                s.append(p+[(i[0].info,i[-1]+t[-1])])

        print(dic)
'''
s=[[(1,0)]]
p = [(1,0)]
s = []
t = (1,0)
a = 1
i = (2r,0),(3r,0)
s = [(1,0)]+[(2,0+0)]
s = [[(1,0),(2,0)]]
i = 3r,0
s = [[(1,0),(3,0)]]
p = [(1,0),(2,0)]
t = (2,0)
a = 2
i = (1r,0),(4r,0)
i = 1r,0
s = [[(1,0),(3,0)],[(1,0),(2,0),(1,0)]]

'''


'''
l=[[(1,0),(2,1),(4,0),(6,0)],[(1,0),(3,0),(6,0)]]
s = [[(1,0)]]
p = [(1,0)]
t = p[-1]
t = (1,0)
a = d[t[0]]
a = 1r
a.children = (2r,0),(3r,0)
s.append(p+[(i[0].info,i[-1]+t[-1]))

'''




G = Graph()
# G.Bfs(1,6)
# G.dijkstra_shortest_path(1,6)
G.path(1,5)










