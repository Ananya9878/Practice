class Node:
    def __init__(self,info=None):
        self.info = info
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
        self.d = {}

    def insert(self,p,c,w):

        if p not in self.d:
            self.d[p] = Node(p)
        p_node = self.d[p]

        if c not in self.d:
            self.d[c] = Node(c)
        c_node = self.d[c]

        if self.root is None:
            self.root = p_node
        p_node.children.append((c_node,w))

    def Display(self):
        if self.root is None:
            return
        z = [self.root]
        while len(z)>0:
            p = z.pop()
            print(p.info)
            for i in p.children:
                z.append(i[0])





        
class Graph:
    def __init__(self):
        self.start = None
        self.d = {}
        f = open('C:/Users/Ananya Sinha/Desktop/Practice/DSA/GRAPH/Shortest Path Algorithm/input1.txt','r')
        v,e = map(int,f.readline().split())
        for i in range(e):
            a,b,w = map(int,f.readline().split())
            self.create(a,b,w)
        
    def create(self,p,c,w):
        if p not in self.d:
            self.d[p] = Node(p)
        p_node = self.d[p]
        
        if c not in self.d:
            self.d[c] = Node(c)
        c_node = self.d[c]
        
        p_node.children.append((c_node,w))
        c_node.children.append((p_node,w))
        
    def mini(self,s):
        m=s[0]
        for i in range(len(s)):
            if s[i][-1]<m[-1]:
                m=s[i]
        return m
        
    def Prim_Mst(self,start,end):
        z = self.d[start]
        s=[(z,0)]
        visited = set()
        mini_tree_sum = 0
        dic={}
        while len(s)>0:
            p = self.mini(s)
            s.remove(p)
            if p[0] in visited:
                continue
            # print(p[0].info,p[1])
            mini_tree_sum+=p[1]


            for i in p[0].children:
                if i[0] not in visited:
                    s.append((i[0],i[-1]))
                    print(p[0].info,i[0].info,i[-1])
                    a,b,w = p[0].info,i[0].info,i[-1]
                    if b in dic:
                        if dic[b][-1] > w:
                            dic[b] = (a,w)
                    else:
                        dic[i[0].info] = (p[0].info,i[-1])

            visited.add(p[0])
        print(mini_tree_sum)
        print(dic)
        return dic

            
            

G = Graph()
d=G.Prim_Mst(0,4)
T = Tree()
for i in d.keys():
    T.insert(d[i][0],i,d[i][1])

T.Display()


        
        
        
        
        