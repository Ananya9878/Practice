class Node:
    def __init__(self,info=None):
        self.info = info
        self.children = []

class Graph:
    def __init__(self):
        self.start = None
        self.d = {}

    def insert_connection(self,p,c,w):
        if p not in self.d:
            self.d[p] = Node(p)
        p_node = self.d[p]

        if c not in self.d:
            self.d[c] = Node(c)
        c_node = self.d[c]

        p_node.children.append((c_node,w))
        c_node.children.append((p_node,w))


    def Dfs(self,start,end):
        t = self.d[start]
        s=[(t,0)]
        visited = set()
        while len(s)>0:
            p = s.pop()
            print(p[0].info,p[1])
            if p[0].info == end:
                break
            if p[0] in visited:
                continue
            for i in p[0].children:
                if i[0] not in visited:
                    s.append((i[0],i[-1]+p[-1]))
            visited.add(p[0])

    def mini(self,p):
        if p is None:
            return
        m = p[0]
        for i in p:
            if i[-1] < m[-1]:
                m = i
        return m

    def dij(self,start,end):
        t=self.d[start]
        s = [(t,0)]
        visited = set()
        while len(s)>0:
            n = self.mini(s)
            print((n[0].info,n[-1]))
            s.remove(n)
            if n[0].info == end:
                break
            if n[0] in visited:
                continue
            for i in n[0].children:
                if i[0] not in visited:
                    s.append((i[0],i[-1]+n[-1]))
            visited.add(n[0])


G = Graph()
print('1 insert')
print('2 dfs')
print('3 dijkstra')

while 1:
    opt = int(input('enter option'))
    if opt == 1:
        a,b,c = list(map(int,input().split()))
        G.insert_connection(a,b,c)
    elif opt == 2:
        s,e = list(map(int,input().split()))
        G.Dfs(s,e)
    elif opt == 3:
        G.dij(1,6)
    else:
        break












