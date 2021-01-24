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


def find_lca(path1,path2):
    k = -1
    while len(path1)>0 and len(path2)>0:
        a = path1.pop()
        b = path2.pop()
        if a == b:
            k = a
        else:
            return k

def main():
    l = list(map(int,input().split()))
    key1,key2 = map(int,input().split())
    T = Tree()
    for i in l:
        T.insert(i)
    path1 = []
    path2 = []
    find_path(T.root,key1,path1)
    find_path(T.root,key2,path2)
    print(path1)
    print(path2)
    print(find_lca(path1,path2))

if __name__ == '__main__':
    main()





