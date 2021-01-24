
class Node:
    def __init__(self,info = None):
        self.info = info
        self.left = None
        self.right = None



class Tree:
    def __init__(self):
        self.root = None

    def display(self):
        if self.root is None:
            return
        n=[self.root]
        while len(n)>0:
            z = []
            # p = n.pop()
            for i in n:
                print(i.info,end=' ')
                if i.left is not None:
                    z.append(i.left)
                if i.right is not None:
                    z.append(i.right)
            print()
            n = z





    def post(self,i, p):
        # print(i,p)
        if len(i) == 0:
            return None
        r = p.pop()
        new_node = Node(r)
        if len(i) == 1:
            return new_node

        k = i.index(r)
        left = i[:k]
        right = i[k + 1:]
        new_node.right = self.post(right, p)
        new_node.left = self.post(left, p)

        return new_node

    def preorder(self,i,p):
        if len(i) == 0:
            return None
        r = p.pop(0)
        new_node = Node(r)
        if len(i) == 1:
            return new_node

        k = i.index(r)
        left = i[:k]
        right = i[k + 1:]

        new_node.left = self.preorder(left, p)
        new_node.right = self.preorder(right, p)
        return new_node




pre = [1,2,4,7,5,8,3,6,9,10]
post = [7,4,8,5,2,9,10,6,3,1]
I = [7,4,2,8,5,1,3,9,6,10]
T = Tree()
T.root = T.preorder(I,pre)
T.display()
T.root = T.post(I,post)
T.display()




