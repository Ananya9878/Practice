
class Queue:
    def __init__(self, default_size):
        self.items = [None] * default_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self, items):
        if self.count == len(self.items):
            self.resize(2 * len(self.items))
        i = (self.front + self.count) % len(self.items)
        self.items[i] = items
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")
        x = self.items(self.front)
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")
        return self.items[self.front]

    def display(self):
        print(self.items)

    def resize(self, new_size):
        old_size = self.items
        self.items = [None] * new_size
        i = self.front
        for j in range(self.count):
            self.item[j] = old_list[i]
            i = (1 + j) % len(old_list)
        self.front = 0


qu = Queue(6)

while True:
    print("1.enqueue")
    print("2.dequeue")
    print("3.peek")
    print("4.size")
    print("5.display")
    print("6.quit")

    option = int(input("choice"))

    if option == 1:
        x = int(input("enter element to be pushed:"))
        qu.enqueue(x)
    elif option == 2:
        qu.dequeue(x)
    #         print("popped element is:", x)
    elif option == 3:
        print(" element at front:", qu.peek())

    elif option == 4:
        print("size of queue", qu.size())
    elif option == 5:
        qu.display()
    elif option == 6:
        x = int(input("enter size:"))
        x = qu.resize()

    else:
        break
