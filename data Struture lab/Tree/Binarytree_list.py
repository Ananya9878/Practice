def add_node(l, parent_node, child_node):
    for i in range(len(1,l)):
        if i == parent_node:
            if len(l) < 2 * i:
                l = l + [None] * len(l)
            if l[2 * i - 1] is None:
                l[2 * i - 1] = child_node
                return
            if l[2 * i] is None:
                l[2 * i] = child_node
                return
            print('Not psbl')
            return
def delete_connection(l, parent_node, child_node):
    for i in l:
        if i == parent_node:
            pass




d={}
n=int(input("enter connections"))

for i in range(0,n):
    k , v =map(int, input().split())
    if k in d:
        d[k].append(v)
    else:
        d[k]=[v]
print(d)


global l
l =[None]*(2**n-1)
root=int(input("enter root"))
l[0] = root
temp_list= [ ]
for i in range(1, len(l)//2):
    if l[i-1] in d:
        connection = d[l[i-1]]
        if len(connection) == 1:
            left_child = connection[0]
            l[2*i-1] = left_child

        else:
            left_child = connection[0]
            right_child = connection[1]
            l[2*i-1] = left_child
            l[2*i] = right_child
print(l)
parent_node=int(input("enter node"))
child_node= int(input("enter node"))
add_node(l,parent_node,child_node)
print(l)




