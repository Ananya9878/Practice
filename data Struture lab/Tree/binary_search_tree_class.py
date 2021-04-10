class Node:
    def __init__(self, data):
        self.value = data
        self.left_child = None
        self.right_child = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None
        self.d = {}

    def insert_node(self, data):
        if self.root is None:
            temp = Node(data)
            self.root = temp
            self.d[data] = temp

        else:
            p = self.root
            while True:
                if p.value < data:
                    if p.right_child is None:
                        temp = Node(data)
                        self.d[data] = temp

                        p.right_child = temp
                        temp.parent = p
                        break
                    else:
                        p = p.right_child
                elif p.value > data:
                    if p.left_child is None:
                        temp = Node(data)
                        self.d[data] = temp

                        p.left_child = temp
                        temp.parent = p
                        break
                    else:
                        p = p.left_child
                else:
                    temp = None

            return temp

    def display(self):
        if self.root is None:
            print("empty")
            return
        queue = [self.root]
        level  = []
        while len(queue)>0:
            for i in queue:
                print(i.value, end= ' ')
                if i.left_child is not None:
                    level.append(i.left_child)
                if i.right_child is not None:
                    level.append(i.right_child)
            print()
            queue = level
            level = []

    def inorder(self, x):
        if x is None:
            return None
        self.inorder(x.left_child)
        print(x.value)
        self.inorder(x.right_child)

    def preorder(self, x):
        if x is None:
            return None
        print(x.value)
        self.preorder(x.left_child)
        self.preorder(x.right_child)

    def postorder(self, x):
        if x is None:
            return None

        self.postorder(x.left_child)
        self.postorder(x.right_child)
        print(x.value)


    def search(self, data):
        p = self.root
        if p is None:
            print("empty")
            return
        while 1:
            if p.value > data:
                if p.left_child is None:
                    return False
                else:
                    p = p.left_child


            elif p.value < data:
                if p.right_child is None:
                    return False
                else:
                    p = p.right_child
            else:

                return True

    def mini(self, root):
        if root == None:
            return None
        p = root
        while p.left_child is not None:
            p = p.left_child
        return p.value



    def delete(self,node_value):
        if node_value not in self.d:
            return None
        node = self.d[node_value]
        self.d.pop(node_value)
        if node.left_child is not None and node.right_child is not None:
            z = node.right_child
            minimum = self.mini(z)
            node.value = minimum
            self.delete(minimum)
            self.d[minimum] = node

        else:
            pr = node.parent
            if node.left_child is not None:
                child = node.left_child
                child.parent = pr
            elif node.right_child is not None:
                child = node.right_child
                child.parent = pr

            else:
                child = None


            if pr is None:
                self.root = child
                return

            if node.value > pr.value:
                pr.right_child = child
            else:
                pr.left_child = child




root = int(input('Enter Root: '))

BT = BST()
BT.insert_node(root)
print('1. Display')
print('2. insert')
print("3. search")
print('4. inorder')
print('5.postorder')
print('6 preorder')
print('7 delete')


while 1:
    opt = input('Enter option: ')
    if opt == '1':
        BT.display()
    elif opt == '2':
        data = int(input("enter element to insert"))
        BT.insert_node(data)
    elif opt == '3':
        data = int(input("enter element to search"))
        print(BT.search(data))
    elif opt =='4':
        BT.inorder(BT.root)
    elif opt == '5':
        BT.postorder(BT.root)
    elif opt == '6':
        BT.preorder(BT.root)
    elif opt == '7':
        data = int(input())
        BT.delete(data)
    else:
        break















