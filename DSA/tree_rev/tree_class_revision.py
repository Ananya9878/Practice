# 1.....insert
# 2.....display
# 3.....delete connection
# 4.....delete node
# 5......search
class Node:
    def __init__(self,value=None):
        self.info = value
        self.children = []

class Tree:
    def __init__(self, root=None):
        self.root = Node(root)
        self.d = {root:self.root}

    def insert_connection(self,parent,child):
        if parent in self.d:
            parent_node = self.d[parent]
        else:
            parent_node = Node(parent)
            self.d[parent] = parent_node

        if child in self.d:
            child_node = self.d[child]
        else:
            child_node = Node(child)
            self.d[child] = child_node

        parent_node.children.append(child_node)


    def display(self):
        if self.root is None:
            print('Tree is empty')

        current_level = [self.root]
        while len(current_level)>0 :
            next_level = []
            for i in current_level:
                print(i.info, end=' ')
                next_level+=(i.children)
            current_level = next_level
            print()


    def search(self,data):
        if self.root is None:
            print('Tree is empty')

        current_level = [self.root]
        while len(current_level) != 0:
            next_level = []
            for i in current_level:
                if data == i.info:
                    print('Yes')
                    return
                next_level+=(i.children)
            current_level = next_level
        print('No')


    def delete_connection(self,parent,child):
        parent_node = self.d[parent]
        child_node = self.d[child]
        if child_node in parent_node.children:
            parent_node.children.remove(child_node)
        else:
            print('Parent not found')

        current_level = [child_node]
        while len(current_level)>0:
            next_level = []
            for i in current_level:
                self.d.pop(i.info)
                next_level+=(i.children)
            current_level = next_level


    def delete_node(self,node_value):
        node = self.d[node_value]
        current_level = [self.root]

        while len(current_level)>0:
            next_level = []
            for i in current_level:
                if node in i.children:
                    parent = i
                    break
                next_level+=(i.children)
            current_level = next_level
        parent.children.remove(node)
        parent.children+=(node.children)

#
# n = int(input('Enter no of connections'))

root = int(input('Enter root'))

T= Tree(root)

print('1 insert connection')
print('2 search')
print('3 display')
print('4 delete connection')
print('5 delete node')

while 1:

    option = int(input('enter option'))
    if option == 1:
        x, y = map(int, input('enter values to insert').split())
        T.insert_connection(x,y)
    elif option == 2:
        T.search((int(input('enter value to search'))))
    elif option ==3:
        T.display()
    elif option == 4:
        a,b = map(int,input('enter connection to delete').split())
        T.delete_connection(a,b)
    elif option == 5:
        T.delete_node(int(input('enter node to delete')))
    else:
        break
