class Node:
    def __init__(self,info=None):
        self.info = info
        self.next = None
        self.prev = None

class llist:
    def __init__(self):
        self.start = None

    def insert_beginning(self,data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start = temp


    def insert_end(self,data):
        temp = Node(data)
        p = self.start
        if p is None:
            self.start = temp
            return
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def insert_after(self,x,data):
        p = self.start
        temp = Node(data)
        if self.start is None:
            return
        while p.info!=x:
            p = p.next
        temp.prev = p
        temp.next = p.next
        p.next.prev = temp
        p.next = temp

    def display(self):
        p = self.start

        while p is not None:
            print(p.info,end=' ')
            p = p.next
        print()

    def delete_node(self,data):
        if self.start is None:
            return
        p = self.start
        while p.info!=data:
            p=p.next
        if p.prev is None:
            self.start = self.start.next
            self.start.prev = None
        else:
            p.prev.next = p.next
        if p.next is None:
            p.prev.next = None
        else:
            p.next.prev = p.prev

    def sort(self):
        p = self.start
        while p is not None:

            if p.prev is None:
                p = p.next
                continue
            elif p.prev.info <= p.info:
                p=p.next
                continue
            else:
                q = p.prev
                while q is not None:
                    if q.info<p.info:
                        self.delete_node(p.info)
                        self.insert_after(q.info,p.info)
                        break
                    q = q.prev
                if q is None:
                    self.delete_node(p.info)
                    self.insert_beginning(p.info)

            p = p.next










l=[4,3,2,10,12,1,5,6]
ll = llist()
for i in l:
    ll.insert_end(i)



ll.display()
# ll.insert_after(2,5)
# ll.delete_node(4)
# ll.delete_node(6)
ll.sort()
ll.display()