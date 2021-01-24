def create_graph():
    f=open('input1.txt','r')
    v,e=map(int,f.readline().split())
    edge_list=[]
    for i in range(e):
        a,b,w = f.readline().split()
        edge_list.append((a,b,int(w)))
        # edge_list.append((b,a,int(w)))
    print(edge_list)
    return edge_list,v

def bellman_ford(g,v,start):
    path_cost={start:0}
    for j in range(v-1):
        for i in g:
            a,b,w = i
            if a in path_cost:
                new_cost = path_cost[a]+w
                if b in path_cost:
                    if new_cost<path_cost[b]:
                        path_cost[b] = new_cost
                else:
                    path_cost[b] = new_cost
    print(path_cost)

def bellman_ford1(g,v,start):
    flag = True
    path_cost=[100000000]*v
    path_cost[start] = 0
    for j in range(v-1):
        flag=True
        for i in g:
            a,b,w=int(i[0]),int(i[1]),i[2]

            new_cost = path_cost[a]+w
            if path_cost[b]>new_cost:
                path_cost[b] = new_cost
                flag=False
        if flag == True:
            break
        print(path_cost)
    if flag:
        print(path_cost)
    else:
        print('Negative cycle')










if __name__ == '__main__':
    g,v=create_graph()
    bellman_ford1(g,v,3)
