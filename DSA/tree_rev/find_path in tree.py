class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return
        z = [self.root]
        while len(z)>0:
            p = z.pop(0)
            if p.left is None:
                p.left = Node(data)
                return
            else:
                z.append(p.left)
            if p.right is None:
                p.right = Node(data)
                return
            else:
                z.append(p.right)


def find_path(root,key,path):
    if root is None:
        return False
    if root.data == key:
        path.append(root.data)
        return True
    a = find_path(root.left,key,path)
    if a is True:
        path.append(root.data)
        return True
    b = find_path(root.right,key,path)
    if b is True:
        path.append(root.data)
        return True
    return False

def main():
    l = list(map(int,input().split()))
    key = int(input())
    T = Tree()
    for i in l:
        T.insert(i)
    path = []
    find_path(T.root,key,path)
    print(path)

if __name__ == '__main__':
    main()





