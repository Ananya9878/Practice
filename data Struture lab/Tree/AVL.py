class Node:
    def __init__(self, data):
        self.value = data
        self.left_child = None
        self.right_child = None
        self.parent = None

class AVL:
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


        self.balance(temp)



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

    def height(self, p):
        if p is None:
            return 0
        hL = self.height(p.left_child)
        hR = self.height(p.right_child)
        return 1+max(hL, hR)

    def factor(self, s):
        lH , rH = self.height(s.left_child), self.height(s.right_child)
        return(lH - rH)

    def balance(self, new_node):
        temp = new_node
        while temp is not None:
            balancing_factor = self.factor(temp)
            if abs(balancing_factor) > 1:
                l = [temp.value]
                if balancing_factor>0:
                    q = temp.left_child
                    l.append(q.value)
                else:
                    q = temp.right_child
                    l.append(q.value)
                balance_factor = self.factor(q)
                if balance_factor>0:
                    q = q.left_child
                    l.append(q.value)
                else:
                    q = q.right_child
                    l.append(q.value)
                l1 = sorted(l)
                # ROOT....................
                r = l1[1]
                r_value = self.d[r]
                r_value.parent = temp.parent
                if temp.parent is not None:
                    if temp.value > temp.parent.value:
                        temp.parent.right_child = r_value
                    else:
                        temp.parent.left_child = r_value
                else:
                    self.root = r_value



                s = r_value.left_child
                r_value.left_child = self.d[l1[0]]
                self.d[l1[0]].parent = r_value

                if s is not None:
                    if s.value != l1[0]:
                        r_value.left_child.right_child = s
                        s.parent = r_value.left_child
                else:
                    r_value.left_child.right_child = s

                s = r_value.right_child
                r_value.right_child = self.d[l1[2]]
                self.d[l1[2]].parent = r_value

                if s is not None:
                    if s.value != l1[2]:
                        r_value.right_child.left_child = s
                        s.parent = r_value.right_child
                else:
                    r_value.right_child.left_child = s
                temp = r_value
            temp = temp.parent






root = int(input("root:"))

AVL = AVL()
AVL.insert_node(root)
print('1. Display')
print('2. insert')
print("3. Height")


while 1:
    opt = input('Enter option: ')
    if opt == '1':
        AVL.display()
    elif opt == '2':
        data = int(input("enter element to insert"))
        AVL.insert_node(data)
    elif opt == '3':
        print(AVL.heiht())




