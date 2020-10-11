class Node:
    def __init__(self, data):
        self.value = data
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
        self.dict = {root: self.root}

    def add_connection(self, parent_node_value, child_node_value):
        if parent_node_value not in self.dict:
           self.dict[parent_node_value] = Node(parent_node_value)
        parent_node = self.dict[parent_node_value]

        if child_node_value not in self.dict:
            self.dict[child_node_value] = Node(child_node_value)
        child_node = self.dict[child_node_value]

        if parent_node.left_child is None:
            parent_node.left_child = child_node

        elif parent_node.right_child is None:
            parent_node.right_child = child_node
        else:
            print("not possible")



    def display(self):
        if self.root is Node:
            print("empty")
            return
        queue = [self.root]
        traverse_level = []

        while len(queue)>0:
            for i in queue:
                print(i.value, end = '')
                if i.left_child is not None:
                    traverse_level.append(i.left_child)
                if i.right_child is not None:
                    traverse_level.append(i.right_child)
                print()
            queue = traverse_level
            traverse_level = []

root = int(input('Enter Root: '))

T = BinaryTree(root)
print('1. Display')
print('2. Add Connection')


while 1:
    opt = input('Enter option: ')
    if opt == '1':
        T.display()
    elif opt == '2':
        parent_node, child_node = map(int, input().split())
        T.add_connection(parent_node, child_node)









