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






G = Graph()
# G.Bfs(1,6)
G.dijkstra(1,6)










