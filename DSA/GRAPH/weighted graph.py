class Node:
    def __init__(self,value=None):
        self.info = value
        self.children = []

class Graph:
    def __init__(self,start=None):
        self.start = start
        self.d ={}

    def insert(self,parent,child,weight):

        if parent not in self.d:
            self.d[parent] = Node(parent)
        parent_node = self.d[parent]
        if child not in self.d:
            self.d[child] = Node(child)
        child_node = self.d[child]

        parent_node.children.append((child_node,weight))
        child_node.children.append((parent_node,weight))


    def display_BFS(self,start):
        if start not in self.d:
            return 0
        s = self.d[start]
        current_level = [s]
        visited = set()
        while len(current_level)>0:
            k = current_level.pop(0)
            print(k.info)
            for j in k.children:
                if j[0] not in visited:
                    print(j[0].info,end=' ')
                    current_level.append(j[0])
                    visited.add(j[0])
            print()
            print('*********************')

    def display_DFS(self,start):
        if start not in self.d:
            return 0
        s = self.d[start]
        current_level = [s]
        visited = set()
        while len(current_level)>0:
            k = current_level.pop()
            print(k.info)
            for j in k.children:
                if j[0] not in visited:
                    print(j[0].info,end=' ')
                    current_level.append(j[0])
                    visited.add(j[0])
            print()

            print('*********************')


    def display_dfs_rec(self,start,visited=None):
        if visited is None:
            visited = []
        if start in visited:
            return
        else:
            visited.append(start)
        print(start)
        s = self.d[start]
        h = s.children
        for i in h[::-1]:
            self.display_dfs_rec(i[0].info,visited)

T = Graph()
print('1 insert')
print('2 display bfs')
print('3 display dfs')
print('4 display dfs recursion')

while 1:
    option = int(input('enter choice'))

    if option == 1:
        a,b = map(int,input('enter 2 element to insert').split())
        T.insert(a,b)
    elif option == 2:
        T.display_BFS(int(input('Enter start:')))
    elif option == 3:
        T.display_DFS(int(input('Enter start:')))
    elif option == 4:
        T.display_dfs_rec(int(input('Enter start node')),[])
    else:
        break