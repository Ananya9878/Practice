class Node:
    def __init__(self,info=None):
        self.info = info
        self.next = None

class Ll:

    def __init__(self):
        self.head = None


    def insert(self,data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return
        p = self.head
        while p.next is not None:
            p=p.next
        p.next = temp

    def display(self):
        if self.head is None:
            print('Empty list')
        p=self.head
        while p is not None:
            print(p.info,end=' ')
            p = p.next
        print()

def merge(ll1,ll2):
    ll3 = Ll()
    p = ll1.head
    q = ll2.head
    while p is not None and q is not None:
        if p.info < q.info:
            ll3.insert(p.info)
            p = p.next
        else:
            ll3.insert(q.info)
            q = q.next
    if p is not None:
        while p is not None:
            ll3.insert(p.info)
            p=p.next
    if q is not None:
        while q is not None:
            ll3.insert(q.info)
            q=q.next
    return ll3






l1=[11,34,50]
l2=[2,4,6,20]
ll1 = Ll()
ll2 = Ll()
for i in l1:
    ll1.insert(i)
for i in l2:
    ll2.insert(i)

ll1.display()
ll2.display()
ll3 = merge(ll1,ll2)
ll3.display()






