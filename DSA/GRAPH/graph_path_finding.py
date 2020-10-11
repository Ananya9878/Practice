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

    def path(self,start,end):
        path1=set()
        route = [[start]]
        i=0
        while i<len(route):
            k =route.pop(i)
            a = self.d[k[-1]]
            s = a.children
            flag = False
            for j in s:
                if j[0].info not in k:
                    route.insert(i,k+[j[0].info])
                    flag = True
                    if j[0].info== end:
                        path1.add(tuple(k+[j[0].info]))
            if flag == False:
                route.insert(i,k)
                i+=1
        print(route)
        # path=set()
        # for i in route:
        #     if end in i:
        #         t = i.index(end)
        #         path.add(tuple(i[:t+1]))
        # print(path)
        print(path1)

    def path1(self, start, end):
        path1 = set()
        route = []
        current_level = [[start]]
        while len(current_level)>0:
            k = current_level.pop()
            a = self.d[k[-1]]
            s = a.children
            flag = False
            for j in s:
                if j[0].info not in k:
                    current_level.append(k + [j[0].info])
                    flag = True
                    if j[0].info == end:
                        path1.add(tuple(k + [j[0].info]))
            if flag == False:
                route.append(k)

        print(route)
        print(path1)
    def check(self,t,v):
        for i in t:
            if i[0] == v:
                return False
        return True

    def path_bfs(self, start, end):
        path1 = set()
        route = []
        current_level = [[(start,0)]]
        while len(current_level) > 0:
            k = current_level.pop(0)
            a = self.d[k[-1][0]]
            s = a.children
            flag = False
            for j in s:
                if self.check(k,j[0].info):
                    b = k +[(j[0].info,k[-1][1]+j[1])]
                    current_level.append(b)
                    flag = True
                    if j[0].info == end:
                        path1.add(tuple(b))
            if flag == False:
                route.append(k)
            print('***',current_level)
        print(route)
        print(path1)



        # route = [[1]]
        # route = [[1,2], [1,4]]
        # route = [[1,2,3], [1,4]]
        # route = [[1,2,3,4], [1,2,3,5],[1,4]]
        # route = [[1,2,3,4,5], [1,2,3,4,7], [1,2,3,5], [1,4]]
        # route = [[1,2,3,4,5,6], [1,2,3,4,7], [1,2,3,4,5],[1,2,3,5] [1,4]]
        # route = [[1,2,3,4,5,6], [1,2,3,4,7], [1,2,3,4,5],[1,2,3,5] ,[1,4]]
        # route = [[1,2,3,4,5,6], [1,2,3,4,7], [1,2,3,4,5,6],[1,2,3,5] [1,4]]
        # route = [[1,2,3,4,5,6], [1,2,3,4,7], [1,2,3,4,5,6],[1,2,3,5,4],[1,2,3,5,6] [1,4]]
        # route = [[1,2,3,4,5,6], [1,2,3,4,7], [1,2,3,4,5,6],[1,2,3,5,4,7],[1,2,3,5,6] [1,4]]
        # route = [[1,2,3,4,5,6], [1,2,3,4,7], [1,2,3,4,5,6],[1,2,3,5,4,7],[1,2,3,5,6] [1,4,3],[1,4,5],[1,4,7]]

T = Graph()
print('1 insert')
print('2 path')
print('3 path1')
print('4 path_bfs')

while 1:
    option = int(input('enter choice'))

    if option == 1:
        a,b,c = map(int,input('enter 3 element to insert').split())
        T.insert(a,b,c)
    elif option == 2:
        a, b = map(int, input('enter 2 element').split())
        T.path(a,b)
    elif option == 3:
        a, b = map(int, input('enter 2 element').split())
        T.path1(a, b)
    elif option == 4:
        a, b = map(int, input('enter 2 element').split())
        T.path_bfs(a, b)
    else:
        break





