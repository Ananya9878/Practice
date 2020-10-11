class Node:
    def __init__(self,info=None):
        self.info = info
        self.children = []

class Graph:
    def __init__(self):
        self.d = {}

    def insert_connection(self,p,c):
        if p not in self.d:
            self.d[p] = Node(p)
        p_node = self.d[p]

        if c not in self.d:
            self.d[c] = Node(c)
        c_node = self.d[c]
        p_node.children.append(c_node)
        c_node.children.append(p_node)

    def Dfs(self,start):
        if start not in self.d:
            return
        p = self.d[start]
        visited = set()
        z = [p]
        while len(z)>0:
            n = z.pop()
            if n in visited:
                continue
            print(n.info)
            # for i in n.children:
            #     z.append(i)
            z = z+n.children
            visited.add(n)

    def Bfs(self, start):
        if start not in self.d:
            return
        p = self.d[start]
        visited = set()
        z = [p]
        while len(z) > 0:
            n = z.pop(0)
            if n in visited:
                continue
            print(n.info)
            # for i in n.children:
            #     z.append(i)
            z = z + n.children
            visited.add(n)
    '''
    [[1]]
    [[1,2],[1,3]]
    [[1,2,5],[1,2,4],[1,3,4],[1,3,6]]
    '''

    def path_find(self,start,end):
        if start not in self.d:
            return
        start_to_end_path = []
        s = [[start]]
        com_path=[]
        visited = set()
        while len(s)>0:
            k = s.pop(0)
            flag = False
            p= self.d[k[-1]]
            for i in p.children:
                if i.info not in k:
                    s.append(k+[i.info])
                    if i.info == end:
                        start_to_end_path.append(k+[i.info])
                    flag = True
            if flag is False:
                com_path.append(k)
        print(start_to_end_path)
        print('&',com_path)

    def path_find_Dfs(self,start,end):
        if start not in self.d:
            return
        start_to_end_path = []
        s = [[start]]
        com_path=[]
        visited = set()
        while len(s)>0:
            k = s.pop()
            flag = False
            p= self.d[k[-1]]
            for i in p.children:
                if i.info not in k:
                    s.append(k+[i.info])
                    if i.info == end:
                        start_to_end_path.append(k+[i.info])
                    flag = True
            if flag is False:
                com_path.append(k)
        print(start_to_end_path)
        print('&',com_path)








G = Graph()
print('1 create')
print('2 dfs')
print('3 Bfs')
print('4 path find')
print('5 path dfs')
while 1:
    option = int(input('enter option'))
    if option == 1:
        p,c = map(int,input('enter 2 nodes to connect:').split())
        G.insert_connection(p,c)
    elif option == 2:
        s = int(input('enter start node'))
        G.Dfs(s)
    elif option == 3:
        s = int(input('enter start node'))
        G.Bfs(s)
    elif option == 4:
        s,e = map(int,input('enter start and end').split())
        G.path_find(s,e)
    elif option == 5:
        s, e = map(int, input('enter start and end').split())
        G.path_find_Dfs(s, e)
    else:
        break


