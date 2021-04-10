class Node:
    def __init__(self,value):
        self.info=value
        self.link=None
class Single:
    def __init__(self,l=[]):
        self.start = None
        for i in  l:
            self.insert(i)

    def display(self):
        p = self.start
        while p is not None:
            print(p.info)
            p = p.link

    def insert(self,data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def delete_node(self,x):
        if self.start is None:
            print('empty')
            return None
        p = self.start
        i = 0
        if x == 1:
            k = self.start.info
            self.start = p.link
            return k
        while p.link is not None:
            i+=1
            if i == x-1:
                break
            p = p.link
        k = p.link.info
        p.link = p.link.link
        return k


def merge(l1,l2):
    l3 = Single()
    p1 = l1.start
    p2 = l2.start
    while p1 is not None and p2 is not None:
        if p1.info <= p2.info:
            k = l1.delete_node(1)
            l3.insert(k)
            p1 = l1.start
        else:
            k = l2.delete_node(1)
            l3.insert(k)
            p2 = l2.start
    while p1 is not None:
        l3.insert(p1.info)
        p1 = p1.link
    while p2 is not None:
        l3.insert(p2.info)
        p2 = p2.link
    return l3


l = [0,2,3]
list = Single(l)
list2 = Single()
l2=[5,7,11]

# for i in l:
#     list.insert(i)
for i in l2:
    list2.insert(i)
l3 = merge(list,list2)
l3.display()

