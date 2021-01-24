def create_graph():
    f = open('input1.txt','r')
    v,e = map(int,f.readline().split())
    edge_list = []
    for i in range(e):
        a,b,c = map(int,f.readline().split())
        edge_list.append((a,b,c))
        # bidirected
        edge_list.append((b,a,c))

    return edge_list,v

def belman(graph,v,start):
    flag = True
    path_cost = [1000]*v
    path_cost[start] = 0
    for j in range(v-1):
        flag = True
        for i in graph:
            a,b,c = i[0],i[1],i[2]
            new_cost = path_cost[a]+c
            if path_cost[b]>new_cost:
                path_cost[b] = new_cost
                flag = False

        if flag == True:
            break
    if flag:
        return path_cost
    else:
        print('Negative Cycle')


def belman2(graph,v,start):
    flag = True
    path_cost = {start:0}
    for j in range(v-1):
        flag = True
        for i in graph:

            a,b,c = i
            if a in path_cost:
                new_cost = path_cost[a]+c
                if b in path_cost:
                    if path_cost[b]>new_cost:
                        path_cost[b]=new_cost
                        flag = False
                else:
                    path_cost[b] = new_cost
                    flag = False
        if flag:
            return path_cost
    if flag:
        return path_cost
    else:
        return 'Negative Cycle'


graph,v=create_graph()

print(belman(graph,v,1))
print(belman2(graph,v,1))