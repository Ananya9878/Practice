class Node:
    def __init__(self,value=None):
        self.info = value
        self.children = []

class Graph:
    def __init__(self,start=None):
        self.start = start
        self.d ={}

    def insert(self,parent,child):

        if parent not in self.d:
            self.d[parent] = Node(parent)
        parent_node = self.d[parent]
        if child not in self.d:
            self.d[child] = Node(child)
        child_node = self.d[child]

        parent_node.children.append(child_node)
        child_node.children.append(parent_node)

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
                if j not in visited:
                    print(j.info,end=' ')
                    current_level.append(j)
                    visited.add(j)
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
                if j not in visited:
                    print(j.info,end=' ')
                    current_level.append(j)
                    visited.add(j)
            print()

            print('*********************')

    def path_search_Dfs(self,start,end):
        if start not in self.d:
            return 0
        # s = self.d[start]
        current_level = [[start]]
        visited_list = set([start])
        while len(current_level)>0:
            k = current_level.pop(0)
            if k[-1] == end:
                print(k)
                return k
            if k[-1] not in visited_list:
                visited_list.add(k[-1])
            h = self.d[k[-1]]
            for i in h.children:
                current_level.insert(0,k+[i.info])

            print(current_level,visited_list)
            # print()
            # print("**************************************")

    def path_search_Bfs(self, start, end):
        if start not in self.d:
            return 0
        # s = self.d[start]
        current_level = [[start]]
        visited_list = set([start])
        while len(current_level)>0:
            k = current_level.pop(0)
            if k[-1] == end:
                print(k)
                return k
            if k[-1] not in visited_list:
                visited_list.add(k[-1])
            h = self.d[k[-1]]
            for i in h.children:
                current_level.append(k+[i.info])

            print(current_level,visited_list)


# root = int(input('enter root'))
T = Graph()
print('1 insert')
print('2 display bfs')
print('3 display dfs')
print('4 Path_search Dfs')
print('5 path bfs')

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
        s,e = map(int,input('enter start and end').split())
        print(T.path_search_Dfs(s,e))
        # l = T.path_search_Dfs(s,e)
        # l1=[]
        # for i in l:
        #     l1.append(i.info)
        # print(l1)
        # l2 = [i.info for i in T.path_search_Dfs(s,e)]
        # print(l2)
    elif option == 5:
        s,e = map(int,input('enter start and end').split())
        print(T.path_search_Bfs(s, e))
        # l2 = [i.info for i in T.path_search_Bfs(s, e)]
        # print(l2)
    else:
        break
