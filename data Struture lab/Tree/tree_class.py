class Node:
    def __init__(self, keys=None):
        self.keys = keys
        self.child = []


class Tree:
    def __init__(self, root):
        self.root = Node(root)
        self.dict = {root: self.root}
        self.height = 0

    def add(self, parent_keys, child_keys):

        if parent_keys not in self.dict:
            self.dict[parent_keys] = Node(parent_keys)
        parent_node = self.dict[parent_keys]

        if child_keys not in self.dict:
            self.dict[child_keys] = Node(child_keys)
        child_node = self.dict[child_keys]

        parent_node.child.append(child_node)



    def display(self):
        height = 0
        if self.root is None:
            print("empty tree")
            return
        queue = [self.root]
        level_traverse = []

        while len(queue) != 0:
            for i in queue:
                print(i.keys, end=' ')
                level_traverse += i.child
            print()
            queue = level_traverse
            level_traverse = []
            height += 1
        self.height = height
        return height

    def search(self, data):
        if self.root is None:
            print("empty tree")
            return
        queue = [self.root]
        level_traverse = []
        while len(queue) != 0:
            for i in queue:
                if i.keys == data:
                    print("data exists")
                    return True
                level_traverse += i.child
            print()
            queue = level_traverse
            level_traverse = []

        print("not exists")
        return False

    def delete(self, parent_keys, child_keys):
        parent_node = self.dict[parent_keys]
        child_node = self.dict[child_keys]
        parent_node.child.remove(child_node)
        queue = [child_node]
        while len(queue) > 0:
            traverse_level = []
            for i in queue:
                print(self.dict.pop(i.keys).keys, end= ' ')
                traverse_level += i.child
            print()
            queue = traverse_level
            traverse_level = []

    def delete_node(self, data):
        if self.root is None:
            print("tree empty")
            return
        queue = [self.root]
        traverse_level = []
        while len(queue)!=0:
            for i in queue:
                data_node=self.dict[data]
                if data_node in i.child:
                    parent_keys = i.keys
                    child_keys = data
                    print(parent_keys, child_keys)
                    self.delete(parent_keys,child_keys)
                    return
                traverse_level += i.child
            queue = traverse_level
            traverse_level=[]




root = int(input('Enter Root: '))

T = Tree(root)
print('1. Display')
print('2. Add Connection')
print('3. Search')

print('4. Delete Connection')
print('5. Delete node')


while 1:
    opt = input('Enter option: ')
    if opt == '1':
        T.display()
    elif opt == '2':
        parent_node, child_node = map(int, input().split())
        T.add(parent_node, child_node)

    elif opt == '3':
        data = int(input('Enter data: '))
        T.search(data)

    elif opt == '4':
        parent_node, child_node = map(int, input('Enter parent node and child node value: ').split())
        T.delete(parent_node, child_node)
    elif opt == '5':
        node = int(input("enter node"))
        T.delete_node(node)

    else:
        break





