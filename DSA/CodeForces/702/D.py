class Node:
    def __init__(self,data=None,height=None):
        self.left = None
        self.right = None
        self.data = data
        self.height = height

def tree(root,left,right):
    if len(left)>0:
        m = max(left)
        i = left.index(m)
        root.left = Node(m,root.height+1)
        res[m] = root.height+1
        tree(root.left,left[:i],left[i+1:])
    if len(right)>0:
        m = max(right)
        i = right.index(m)
        root.right = Node(m,root.height+1)
        res[m] = root.height + 1
        tree(root.right,right[:i],right[i+1:])

for i in range(int(input())):
    n = input()
    l = list(map(int,input().split()))
    m = max(l)
    i = l.index(m)
    left = l[:i]
    right = l[i+1:]
    root = Node(m,0)
    res={m:0}
    tree(root,left,right)
    for i in l:
        print(res[i],end=' ')
    print()


