class Node:

    def __init__(self, value):
        self.info = value
        self.prev = None
        self.next = None


class doubly:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("empty")
            return
        print("List is: ")
        p = self.start
        while p is not None:
            print(p.info, " ", end='')
            p = p.next
        print()
        print("*" * 20)

    def insert_beginning(self, data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start = temp

    def insert_empty(self, data):
        temp = Node(data)
        self.start = temp

    def insert_end(self, data):
        temp = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def create_list(self):
        n = int(input("enter no of nodes"))
        if n == 0:
            return
        data = int(input("enter the first element"))
        self.insert_empty(data)

        for i in range(n - 1):
            data = int(input("enter next element"))
            self.insert_end(data)

    def insert_after(self, data, x):
        p = self.start
        if self.start is None:
            print("empty")
            return
        while p.info != x:
            temp = Node(data)
            p = p.next
        temp.prev = p
        temp.next = p.next
        if p.next is not None:
            p.next.prev = temp
        p.next = temp

    def insert_before(self, data, x):
        p = self.start
        if self.start is None:
            print("empty")
            return

        if p.info == x:
            temp = Node(data)
            temp.next = self.start
            self.start.prev = temp
            self.start = temp
            return

        while p.info != x:
            p = p.next

        temp = Node(data)
        temp.prev = p.prev
        temp.next = p
        p.prev.next = temp
        p.prev = temp

    def delete_first(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return
        self.start = self.start.next
        self.start.prev = None

    def delete_last(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return
        p = self.start
        while p.next != None:
            p = p.next
        p.prev.next = None

    def delete_node(self, x):
        if self.start is None:
            return
        if self.start.next is None:
            if self.start.info == x:
                self.start = None
                return
        if self.start.info == x:
            self.start = self.start.next
            self.start.prev = None
            return
        p = self.start.next
        while p.next is not None:
            if p.info == x:
                break
            p = p.next

        if p.next is not None:
            p.prev.next = p.next
            p.next.prev = p.prev
            return

        if p.info == x:
            p.prev.next = None

    def reversed(self):
        if self.start is None:
            return
        p1 = self.start
        p2 = p1.next
        p1.next = None
        p1.prev = p2
        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.start = p1


list = doubly()
list.create_list()

while True:

    print("1.Display list")
    print("2.insert empty")
    print("3.insert beginning")
    print("4.insert end")
    print("5.insert after")
    print("6.Add before particular node")
    print("7.delet first")
    print("8.delet last")
    print("9.delet node")
    print("10 reverse")

    option = int(input("choice"))

    if option == 1:
        list.display_list()

    elif option == 2:
        data = int(input("enter element:"))
        list.insert_empty(data)
    elif option == 3:
        data = int(input("enter element:"))
        list.insert_beginning(data)
    elif option == 4:
        data = int(input("enter element:"))
        list.insert_end(data)


    elif option == 5:
        data, x = map(int, input("data, x").split())
        list.insert_after(data, x)
    elif option == 6:
        data, x = map(int, input("data, x").split())
        list.insert_before(data, x)

    elif option == 7:
        list.delete_first()
    elif option == 8:
        list.delete_last()

    elif option == 9:
        data = int(input("enter element to del:"))

        list.delete_node(data)
    elif option == 10:
        list.reverse()

    else:
        break


