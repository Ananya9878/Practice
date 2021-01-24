class Node:
    def __init__(self,info=None):
        self.info = info
        self.children = []

class Tree:
    def __init__(self,root=None):
        self.root = Node(root)
        if root is not None:
            self.d = {root:self.root}
        else:
            self.d = {}


    def insert(self,p,c,w):
        if self.root is None:
            self.root = Node(p)
            self.d[p] = self.root
        if p not in self.d:
            self.d[p] = Node(p)
        p_node = self.d[p]

        if c not in self.d:
            self.d[c] = Node(c)
        c_node = self.d[c]

        p_node.children.append((c_node,w))

    def display(self):
        s = [(self.root,0)]
        while len(s)!=0:
            z=[]
            for i in s:
                print((i[0].info,i[1]),end=' ')
                z+=i[0].children
            print()
            s = z

def create():
    f = open('input.txt','r')
    v,e = map(int,f.readline().split())
    G={}
    for i in range(e):
        a,b,c = map(int,f.readline().split())
        if a not in G:
            G[a] = [(b,c)]
        else:
            G[a].append((b,c))

        if b not in G:
            G[b] = [(a,c)]
        else:
            G[b].append((a,c))

    return G


def mini(s):
    m = s[0]
    for i in range(len(s)):
        if s[i][-1]<m[-1]:
            m = s[i]
    return m



def Prim(G,start):
    T = Tree(start)
    s = [(None,start,0)]
    visited = set()
    cost=0
    while len(s)>0:
        p = mini(s)
        s.remove(p)
        if p[1] in visited:
            continue
        # print(p)
        if p[0] is not None:
            T.insert(p[0],p[1],p[2])
        cost+=p[-1]

        for i in G[p[1]]:
            if i[0] not in visited:
                s.append((p[1],i[0],i[-1]))

        visited.add(p[1])
    # print(cost)
    return T,cost


G = create()
T,cost = Prim(G,0)
print(cost)
T.display()
# T = Tree()
# T.insert(1,2,1)
# T.insert(1,3,1)
# T.insert(2,4,1)
# T.insert(2,5,1)
# T.insert(3,6,1)
# T.display()





