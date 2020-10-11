class Node:
    def __init__(self,value):
        self.info = value
        self.pre = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None

    def display(self):
        pass
    def search(self,data):
        pass

    def insert_in_beginning(self,data):
        pass

    def insert_end(self,data):
        pass
    def create_list(self):
        pass
    def insert_after(self,data):
        pass
    def insert_before(self,data):
        pass
    def delete_first_node(self):
        pass
    def delete_in_between_nodes(self):
        pass
    def delete_last_node(self):
        pass

    def reverse_list(self):
        pass

SL = DoublyLinkedList()

print('1.display')
print('2.insert in beginning')
print('3.insert end')
print('4 insert after')
print('5 insert before')
print('6 search')
print('7 create list')
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
        SL.create_list()
    elif option == 8:
        SL.delete_first_node()
    elif option == 9:
        SL.delete_last_node()
    elif option == 10:
        SL.delete_between_nodes(int(input('enter element to delete:')))
    else:
        break