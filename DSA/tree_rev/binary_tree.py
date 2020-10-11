class Node:
    def __init__(self,value=None):
        self.info = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self,root=None):
        self.root = Node(root)
        self.d = {root:self.root}

    def insert(self,parent,child):
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
            print('Parent Node not found')


    def insert_node(self,child):
        current_level = [self.root]
        child_node = Node(child)
        self.d[child] = child_node
        while len(current_level)>0:
            next_level = []
            for i in current_level:
                if i.left_child is not None:
                    next_level.append(i.left_child)
                else:
                    i.left_child = child_node
                    return
                if i.right_child is not None:
                    next_level.append(i.right_child)
                else:
                    i.right_child = child_node
                    return
            current_level = next_level


    def display(self):
        if self.root is None:
            print('Tree is empty')

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
        if self.root is None:
            print('Tree is empty')

        current_level = [self.root]
        while len(current_level)>0:
            next_level = []
            for i in current_level:
                if data == i.info:
                    print('Yes')
                    return
                if i.left_child is not None:
                    next_level.append(i.left_child)
                if i.right_child is not None:
                    next_level.append(i.right_child)
            current_level = next_level
        print('No')


    def height1(self):
        c=0
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
            c+=1
            print(c)

    def height_rec(self,p):
        if p is None:
            return 0
        hL = self.height_rec(p.left_child)
        hR = self.height_rec(p.right_child)
        return 1+max(hL,hR)


    def delete_connection(self,parent,child):
        parent_node = self.d[parent]
        child_node = self.d[child]
        if parent_node.left_child == child_node:
            parent_node.left_child = None
        elif parent_node.right_child == child_node:
            parent_node.right_child = None
        else:
            print('Not exists')

        current_level = [child_node]
        while len(current_level)>0:
            next_level = []
            for i in current_level:
                self.d.pop(i.info)
                if i.left_child is not None:
                    next_level.append(i.left_child)
                if i.right_child is not None:
                    next_level.append(i.right_child)

            current_level = next_level

    def delete_node(self, child):
        child_node = self.d[child]
        self.d.pop(child)
        # if child_node == self.root:
        #     if self.root.left_child is not None:
        #         self.root = self.root.left_child
        #         if child_node.right_child is not None:
        #             self.insert_node(child_node.right_child.info)
        #
        #     elif self.root.right_child is not None:
        #         self.root = self.root.right_child
        #         if child_node.left_child is not None:
        #             self.insert_node(child_node.left_child.info)
        #     return
        current_level = [self.root]
        # flag = True
        while len(current_level) > 0:
            next_level = []
            for i in current_level:
                if i.left_child is not None:
                    next_level.append(i.left_child)
                    if i.left_child is child_node:
                        i.left_child = None
                        # flag = False
                        next_level=[]
                        break

                if i.right_child is not None:
                    next_level.append(i.right_child)
                    if i.right_child is child_node:
                        i.right_child = None
                        # flag = False
                        next_level=[]
                        break


            current_level = next_level
            # if flag == False:
            #     break
        if child_node.left_child is not None:
            self.insert_node(child_node.left_child.info)
        if child_node.right_child is not None:
            self.insert_node(child_node.right_child.info)


root = int(input('enter root'))
BT = BinaryTree(root)
print('1 insert connection')
print('2 display')
print('3 insert node')
print('4 delete connection')
print('5 delete node')
print('6 search')
print('7 height')
print('8 height recursion')
while 1:
    option = int(input('Enter option:'))
    if option == 1:
        a,b = map(int,input('Enter value to insert').split())
        BT.insert(a,b)
    elif option == 2:
        BT.display()
    elif option == 3:
        BT.insert_node(int(input('Enter node value to insert:')))
    elif option == 4:
        a, b = map(int, input('Enter value to insert').split())
        BT.delete_connection(a, b)
    elif option == 5:
        BT.delete_node(int(input('enter node to delete')))
    elif option == 6:
        BT.search(int(input('Enter value to search')))
    elif option == 7:
        BT.height1()
    elif option == 8:
        print(BT.height_rec(BT.root))
    else:
        break
















