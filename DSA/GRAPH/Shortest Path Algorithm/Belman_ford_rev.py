def create():
    edge_list = []
    f = open('input1.txt','r')
    v,e = map(int,f.readline().split())

    for i in range(e):
        a, b, c = map(int, f.readline().split())
        edge_list.append((a,b,c))
        edge_list.append((b,a,c))

    return edge_list,v

def bellman_ford(g,v,start):
    p=[10000000]*v
    p[start] = 0
    flag = False
    for j in range(v-1):
        flag = False
        for i in g:
            s,d,w = i[0],i[1],i[2]
            new_cost = p[s]+w
            if p[d]>new_cost:
                p[d] = new_cost

                flag = True

            # print(s,d,w,new_cost,p)
        # print('************')
        if flag is False:
            print(start,p)
            return

    if flag:
        print('Negative cycle')


g,v = create()
bellman_ford(g,v,0)
bellman_ford(g,v,1)
bellman_ford(g,v,2)
bellman_ford(g,v,3)
bellman_ford(g,v,4)
bellman_ford(g,v,5)






