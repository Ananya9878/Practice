class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class Single:
    def __init__(self):
        self.start = None

    def display(self):
        if self.start is None:
            print('Empty linked list')
        p = self.start
        while p is not None:
            print(p.info,end=' ')
            p = p.link


    def count_nodes(self):
        if self.start is None:
            return 0
        c=0
        p = self.start
        while p is not None:
            c+=1
            p = p.link
        print(c)


    def search(self,x):
        if self.start is None:
            print('Empty linked list')
        p = self.start
        while p.link is not None:
            p = p.link
            if x == p.info:
                print('Yes')
                return
        print('Not found')


    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp


    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp



    def insert_after(self,x,data):
        temp = Node(data)
        p = self.start
        while p is not None:
            p = p.link
            if p.info == x:
                temp.link = p.link
                p.link = temp
                return



    def insert_before(self,x,data):

        if self.start.info == x:
            self.insert_in_beginning(data)
            return
        temp = Node(data)
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                temp.link = p.link
                p.link = temp
                return
        p = p.link



    def delete_first_node(self):
        self.start = self.start.link


    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.link is None:
            self.start = None
            return
        p = self.start
        while p is not None:
            if p.link.link is None:
                p.link= None
                return
            p = p.link

    def delete_between_nodes(self,x):
        p = self.start
        while p.link is not None:

            if p.link.info == x:
                p.link = p.link.link
                return
            p = p.link

    def reverse_linked_list(self):
        pass

SL = Single()

print('1.display')
print('2.insert in beginning')
print('3.insert end')
print('4 insert after')
print('5 insert before')
print('6 search')
print('7 count')
print('8 delete first')
print('9 delete last')
print('10 delete between nodes')


while 1:

    option = int(input('Enter choice:'))

    if option == 1:
        SL.display()
    elif option == 2:
        SL.insert_in_beginning(int(input('enter data to insert in beginning:')))
    elif option == 3:
        SL.insert_at_end(int(input('enter data to insert at end:')))
    elif option == 4:
        a,b = map(int,input('enter data to insert after data:').split())
        SL.insert_after(a,b)
    elif option == 5:
        a,b = map(int,input('enter data to insert before data:').split())
        SL.insert_before(a,b)
    elif option == 6:
        SL.search(int(input('enter element to search:')))
    elif option == 7:
        SL.count_nodes()
    elif option == 8:
        SL.delete_first_node()
    elif option == 9:
        SL.delete_last_node()
    elif option == 10:
        SL.delete_between_nodes(int(input('enter element to delete:')))
    else:
        break











