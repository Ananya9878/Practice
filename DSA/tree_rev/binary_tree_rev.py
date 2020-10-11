class Node:
    def __init__(self,value=None):
        self.info = value
        self.left_child = None
        self.right_child = None

class binaryTree:
    def __init__(self,root=None):
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
        if parent_node.left_child is None:
            parent_node.left_child = child_node
        elif parent_node.right_child is None:
            parent_node.right_child = child_node
        else:
            print('Node not found')


    def insert_node(self,child):
        child_node = Node(child)
        self.d[child] = child_node
        current_level = [self.root]
        while len(current_level)>0:
            next_level = []
            for i in current_level:
                if i.right_child is not None:
                    next_level.append(i.right_child)
                else:
                    i.right_child = child_node
                    return
                if i.left_child is not None:
                    next_level.append(i.left_child)
                else:
                    i.left_child = child_node
                    return
            current_level = next_level


    def display(self):
        if self.root is None:
            return 0
        current_level = [self.root]
        while len(current_level)>0:
            next_level = []
            for i in current_level:
                print(i.info,end=' ')
                if i.left_child is not None:
                    next_level.append(i.left_child)
                if i.right_child is not None:
                    next_level.append(i.right_child)
            current_level = next_level
            print()


    def search(self,data):
        def display(self):
            if self.root is None:
                return 0
            current_level = [self.root]
            while len(current_level) > 0:
                next_level = []
                for i in current_level:
                    if data == i.info:
                        print('YES')
                        return
                    if i.left_child is not None:
                        next_level.append(i.left_child)
                    if i.right_child is not None:
                        next_level.append(i.right_child)
                current_level = next_level
            print('NO')

    def height(self,h):
        if h is None:
            return 0
        hl = self.height(h.left_child)
        hr = self.height(h.right_child)
        return 1+max(hl,hr)

    def delete_connection(self,parent,child):
        parent_node = self.d[parent]
        child_node = self.d[child]
        if parent_node.left_child == child_node:
            parent_node.left_child = None
        elif parent_node.right_child == child_node:
            parent_node.right_child = None
        else:
            print('Node does not exists')

        current_level = [self.root]
        while len(current_level)>0:
            next_level = []
            for i in current_level:
                self.d.pop(i.info)
                if i.left_child is not None:
                    next_level.append(i.left_child)
                if i.right_child is not None:
                    next_level.append(i.right_child)
            current_level = next_level


root = int(input('enter root'))
BT = binaryTree(root)

print('1 insert connection')
print('2 display')
print('3 insert node')
print('4 delete connection')
print('5 search')
print('6 height')

while 1:

    option = int(input('Enter option:'))
    if option == 1:
        a,b = map(int,input('Enter value to insert').split())
        BT.insert_connection(a,b)
    elif option == 2:
        BT.display()
    elif option == 3:
        BT.insert_node(int(input('Enter node value to insert:')))
    elif option == 4:
        a, b = map(int, input('Enter value to insert').split())
        BT.delete_connection(a, b)
    elif option == 5:
        BT.search(int(input('Enter value to search')))
    elif option == 6:
        print(BT.height(BT.root))
    else:
        break

