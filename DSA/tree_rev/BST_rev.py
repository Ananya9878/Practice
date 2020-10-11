class Node:
    def __init__(self,value=None):
        self.info = value
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self,root):
        self.root = Node(root)

    def insert_node(self,data):
        temp = Node(data)
        if self.root is None:
            self.root = temp
        p = self.root
        while p is not None:
            if p.info>=data:
                if p.left_child is None:
                    p.left_child = temp
                    return
                else:
                    p = p.left_child
            else:
                if p.right_child is None:
                    p.right_child = temp
                    return
                else:
                    p = p.right_child


    def insert_rec(self,data,p):
        temp = Node(data)
        if p is None:
            p = temp
        elif p.info>=data:
            if p.left_child is None:
                p.left_child = temp
                return
            else:
                self.insert_rec(data,p.left_child)
        else:
            if p.right_child is None:
                p.right_child = temp
                return
            else:
                self.insert_rec(data,p.right_child)

    def display(self):
        if self.root is None:
            return 0
        current_level = [self.root]
        c=0
        while len(current_level)>0:
            next_level = []
            for i in current_level:
                print(i.info,end='')
                if i.left_child is not None:
                    next_level.append(i.left_child)
                if i.right_child is not None:
                    next_level.append(i.right_child)

            current_level = next_level
        print()


    def search(self,data):
        p = self.root
        if p is None:
            print('NO')
            return

        while p is not None:
            if p.info>data:
                p = p.left_child
            elif p.info < data:
                p = p.right_child
            else:
                print('Yes')
                return


    def search_rec(self,data,p):
        if p is None:
            print('No')
            return None
        elif p.info == data:
            print('yes')
            return
        elif p.info>data:
            return self.search_rec(data,p.left_child)
        else:
            return self.search_rec(data,p.right_child)


    def inorder_successor(self,p):
        while p.left_child is not None:
            p = p.left_child
        return p
    #     if p.left_child is None:
    #         return p
    #     return self.inorder_successor(p.left_child)



    def delete_node(self,data):
        parent = None
        child = None
        flag = None
        if self.root.info == data:
            child = self.root
        else:
            p = self.root
            while p is not None:
                if p.left_child.info == data:
                    parent = p
                    child = p.left_child
                    flag = False
                    break
                elif p.right_child.info == data:
                    parent = p
                    child = p.right_child
                    flag = True
                    break
                else:
                    if p.info>=data:
                        p = p.left_child
                    else:
                        p = p.right_child

        if child.right_child is None and child.left_child is None:
            if flag is None:
                self.root = None
            elif flag is False:
                parent.left_child = None
            else:
                parent.right_child = None

        elif child.left_child is None:
            if flag is None:
                self.root = self.root.right_child
            elif flag is False:
                parent.left_child = child.right_child
            else:
                parent.right_child = child.right_child

        elif child.right_child is None:
            if flag is None:
                self.root = self.root.left_child
            elif flag is False:
                parent.left_child = child.left_child
            else:
                parent.right_child = child.left_child

        else:
            d = self.inorder_successor(child.right_child)
            self.delete_node(d.info)
            child.info = d.info

    def pre_order(self,p):
        if p is None:
            return
        print(p.info)
        self.pre_order(p.left_child)
        self.pre_order(p.right_child)


    def in_order(self,p):
        if p is None:
            return
        self.in_order(p.left_child)
        print(p.info)
        self.in_order(p.right_child)


    def post_order(self,p):
        if p is None:
            return
        self.post_order(p.left_child)
        self.post_order(p.right_child)
        print(p.info)


    def height(self,p):
        if p is None:
            return 0
        hL = self.height(p.left_child)
        hR = self.height(p.right_child)
        return 1+max(hL,hR)


root = int(input('Enter root'))
B = BST(root)

print('1 display')
print('2 insert_node')
print('3 insert_rec')
print('4 search')
print('5 searchRec')
print('6 pre_order')
print('7 post_order')
print('8 in_order')
print('9 delete_node')
print('10 height')

while 1:
    option = int(input('Enter option:'))

    if option == 1:
        B.display()
    elif option == 2:
        B.insert_node(int(input('enter node')))
    elif option == 3:
        B.insert_rec(int(input('enter is insert')), B.root)
    elif option == 4:
        B.search(int(input('enter element to search')))
    elif option == 5:
        B.search_rec(int(input('element to search')),B.root)
    elif option == 6:
        B.pre_order(B.root)
    elif option == 7:
        B.post_order(B.root)
    elif option == 8:
        B.in_order(B.root)
    elif option == 9:
        B.delete_node(int(input('enter data to delete')))
    elif option == 10:
        print(B.height(B.root))
    else:
        break





