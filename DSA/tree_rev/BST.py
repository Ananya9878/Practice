class Node:
    def __init__(self,value=None):
        self.info = value
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self,root):
        self.root = Node(root)

    def display(self):
        if self.root is None:
            return 0
        current_level = [self.root]
        while len(current_level) > 0:
            next_level = []
            for i in current_level:
                print(i.info,end=' ')
                if i.left_child is not None:
                    next_level.append(i.left_child)
                if i.right_child is not None:
                    next_level.append(i.right_child)
            current_level = next_level
            print()


    def insert_node(self,data):
        temp = Node(data)
        if self.root is None:
            self.root = temp
        current_level = [self.root]
        while len(current_level)>0:
            next_level = []
            for i in current_level:
                if i.info >= data:
                    if i.left_child is None:
                        i.left_child = temp
                        return
                    else:
                        next_level.append(i.left_child)
                else:
                    if i.right_child is None:
                        i.right_child = temp
                        return
                    else:
                        next_level.append(i.right_child)
            current_level = next_level

    def insert1(self,data):
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
            return
        # else:
        #     print(data,p.info)
        if p.info >= data:
            if p.left_child is None:
                p.left_child = temp
                return
            else:
                self.insert_rec(data,p.left_child)
                # if p.left_child is not None:
                    # print(data,p.left_child.info)
        else:
            if p.right_child is None:
                p.right_child = temp
                return
            else:
                self.insert_rec(data,p.right_child)
                # if p.right_child is not None:
                #     print(data,p.right_child.info)
        print(data,p.info)
        self.balance(p)

    def search(self,data):
        if self.root is None:
            return 0
        current_level = [self.root]
        while len(current_level)>0:
            next_level = []
            for i in current_level:
                if i.info == data:
                    print('Yes')
                    return
                if i.info >= data:
                    if i.left_child is not None:
                        next_level.append(i.left_child)
                else:
                    next_level.append(i.right_child)
            current_level = next_level
            print(current_level)
        print('Not found')
        
    def search1(self,data):
        if self.root is None:
            return 0
        p = self.root
        while p is not None:
            if p.info == data:
                print('Yes')
                return True
            if p.info >= data:
                p = p.left_child
            else:
                p = p.right_child
        print('no')
        return False


    def search_recursion(self,p,data):
        if p is None:
            print('Not found')
            return False
        if p.info == data:
            print('Yes')
            return True
        elif p.info>=data:
            self.search_recursion(p.left_child,data)
        else:
            self.search_recursion(p.right_child,data)

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


    def inorder_successor(self,node):
        # print(node, node.info)
        if node.left_child is None:
            return node
        return self.inorder_successor(node.left_child)


    def delete_node(self,data):
        if self.root is None:
            return
        parent = None
        child = None
        flag = None
        if data == self.root.info:
            child = self.root
        else:
            p = self.root
            while p is not None:
                if p.left_child.info == data:
                    parent = p
                    child = parent.left_child
                    flag = False
                    break
                elif p.right_child.info == data:
                    parent = p
                    child = parent.right_child
                    flag = True
                    break
                else:
                    if p.info>=data:
                        p = p.left_child
                    else:
                        p = p.right_child
        if child.left_child is None and child.right_child is None:
            if flag is None:
                self.root = None
            elif flag is False:
                parent.left_child = None
            else:
                parent.right_child = None
        elif child.left_child is None:
            if flag is None:
                self.root = child.right_child
            elif flag is False:
                parent.left_child = child.right_child
            else:
                parent.right_child = child.right_child
        elif child.right_child is None:
            if flag is None:
                self.root = child.left_child
            elif flag is False:
                parent.left_child = child.left_child
            else:
                parent.right_child = child.left_child

        else:
            node = self.inorder_successor(child.right_child)
            self.delete_node(node.info)
            child.info = node.info


    def height(self,p):
        if p is None:
            return 0
        hL = self.height(p.left_child)
        hR = self.height(p.right_child)
        return 1+max(hL,hR)

    def balance_factor(self,p):
        hl,hr = self.height(p.left_child) , self.height(p.right_child)
        return(hl-hr)

    def balance(self,p):
        balancing_fac = self.balance_factor(p)
        if abs(balancing_fac) < 2:
            return p
        l=[(p.info,p)]
        while len(l)<3:
            if balancing_fac>0:
                l.append((p.left_child.info,p.left_child))
                p = p.left_child
            else:
                l.append((p.right_child.info,p.right_child))
                p = p.right_child

            balancing_fac = self.balance_factor(p)
        # print(l)

        k = l[0][1]
        new_node = Node(k.info)
        new_node.left_child = k.left_child
        new_node.right_child = k.right_child
        l1 = l[:]
        l1[0] = (new_node.info,new_node)
        l1.sort()
        k.info = l1[1][0]
        k.left_child = l1[0][1]
        k.right_child = l1[2][1]
        t = l1[1][1]
        if k.left_child != t.left_child:
            k.left_child.right_child = t.left_child
        if k.right_child != t.right_child:
            k.right_child.left_child = t.right_child



root = int(input('Enter root'))
B = BST(root)

print('1 display')
print('2 insert_node')
print('3 search')
print('4 searchRec')
print('5 height')
print('6 preorder')
print('7 postorder')
print('8 inorder')
print('9 delete')
print('10 insert_rec')
print('11 insertBst')
print('12 search1')

while 1:
    option = int(input('Enter option:'))

    if option == 1:
        B.display()
    elif option == 2:
        B.insert_node(int(input('enter node')))
    elif option == 3:
        B.search(int(input('enter element to search')))
    elif option == 4:
        B.search_recursion(B.root,int(input('element to search')))
    elif option == 5:
        print(B.height(B.root))
    elif option == 6:
        B.post_order(B.root)
    elif option == 7:
        B.pre_order(B.root)
    elif option == 8:
        B.in_order(B.root)
    elif option == 9:
        B.delete_node(int(input('enter data to delete')))
    elif option == 10:
        B.insert_rec(int(input('enter is insert')),B.root)
    elif option == 11:
        B.insert1(int(input('enter element to insert')))
    elif option == 12:
        B.search1(int(input('enter element to search')))
    else:
        break

