'''
A B
B D
B T
D T
C D
C B
C A
S C
S A

S...0
A...inf,5,0
B...inf,6,2,1
C...inf,-2
D...inf,5,2,0
T...inf,9,8,1

0 1
1 2
2 3
3 0

0...0,-2,-4,-6
1...inf,1,-1,-3
2...inf,0,-2,-4
3..inf,-1,-3,-5
'''


class Graph:
    def __init__(self):
        self.no_of_node = int(input('enter nodes'))
        self.shortest_path = [1000000]*self.no_of_node
        no_of_edge = int(input('enter no of edge'))
        self.edges = []

        f = open('input.txt','r')
        for i in range(no_of_edge):
            a,b,c = map(int,f.readline().split())
            self.edges.append((a,b,c))
            # self.insert_connection(a,b,c)


    def bellman_ford(self,start):
        self.shortest_path[start-1] = 0
        for i in range(self.no_of_node-1):
            for edge in self.edges:
                # print(edge)
                a,b,c = edge
                if self.shortest_path[a-1]+c < self.shortest_path[b-1]:
                    self.shortest_path[b-1] = self.shortest_path[a-1]+c
            print(self.shortest_path)

G = Graph()

G.bellman_ford(int(input('start')))






