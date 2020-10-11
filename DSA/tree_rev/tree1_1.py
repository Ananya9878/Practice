class Node:
    def __init__(self, value=None):
        self.info=value
        self.children=[]

class tree:
    def __init__(self,root=None):
        self.root = Node(root)
        self.d = {root:self.root}
        #  /////////////////////////////////
        # new_node = Node(root)
        # self.d = {}
        # self.d[root] = new_node
        # self.root = new_node
        # //////////////////////////////////

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
        # c=0
        if self.root is None:
            return 0
        current_level = [self.root]
        while len(current_level)!=0:
            next_level = []
            for i in current_level:
                print(i.info,end=' ')
                next_level+=(i.children)
            current_level = next_level
            # c+=1
            print()
        # print(c)

    def delete_connection(self,parent,child):
        parent_node = self.d[parent]
        child_node = self.d[child]
        if child_node in parent_node.children:
            parent_node.children.remove(child_node)
        else:
            print('Connection Not Found')
        current_node = [child_node]
        while len(current_node)>0:
            next_level = []
            for i in current_node:
                self.d.pop(i.info)
                next_level+=(i.children)
            current_node = next_level

        # print(parent_node.children)
        # print(child_node)
    def delete_node(self,node_value):
        node = self.d[node_value]
        parent = None
        # /////////////////////////////////////
        current_level = [self.root]
        while len(current_level)>0:
            next_level = []
            for i in current_level:
                if node in i.children:
                    parent = i
                    break
                next_level+=(i.children)
            current_level = next_level
        # ////////////////////////////////////////////
        if parent is not None:
            parent.children.remove(node)
            parent.children+=(node.children)

    def search(self, data):
        if self.root is None:
            return 0
        current_level = [self.root]
        while len(current_level) != 0:
            next_level = []
            for i in current_level:
                if data == i.info:
                    print('Yes')
                    return True
                next_level += (i.children)
            current_level = next_level
        print('No')
        return False


    def height(self):
        if self.root is None:
            return 0
        c=0
        current_level = [self.root]
        while len(current_level) != 0:
            next_level = []
            for i in current_level:
                next_level += (i.children)
            current_level = next_level
            c+=1
        print(c)

n = int(input('enter no of nodes:'))
root = int(input('enter root'))
T = tree(root)

# for i in range(n-1):
#     a,b = map(int,input().split())
#     T.insert_connection(a,b)
# T.display()
# T.height()
# T.search(int(input("enter element to search")))
# T.delete_connection(int(input('parent')),int(input('child')))
# T.display()
print('1 insert')
print('2 search')
print('3 display')
print('4 delete connection')
print('5 delete node')

while 1:
    option = int(input('enter option'))
    if option == 1:
        a, b = map(int, input('enter values to insert').split())
        T.insert_connection(a,b)
    elif option == 2:
        T.search((int(input('enter value to search'))))
    elif option ==3:
        T.display()
    elif option == 4:
        a,b = map(int, input('enter values to insert').split())
        T.delete_connection(a,b)
    elif option == 5:
        a = int(input('enter node to delete'))
        T.delete_node(a)
    else:
        break







