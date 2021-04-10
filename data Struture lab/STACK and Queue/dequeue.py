class Deque:
    def __init__(self, default_size):
        self.items = [] * default_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def insert_front(self, items):
        if self.count == len(self.size):
            self.resize(2 * len(self.items))
        self.front = (self.front - 1) % len(self.items)
        self.items[self.front] = items
        self.count += 1

    def insert_rer(self, items):
        if self.count == len(self.size):
            self.resize(2 * len(self.items))
        i = (self.front + self.count) % len(self.item)
        self.items[i] = items
        self.count += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError("empty")
        x = self.items[self.front]
        self.items[self.front]
        self.items[self.front] = None

        self.front = (self.front + 1) % len(self.items)
        self.count += 1
        return x

    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError("empty")
        rear = (self.front + self.count - 1) % len(self.items)
        x = self.items[rear]
        self.items[rear] = None
        self.count -= 1
        return x

    def fisrt(self):
        if self.is_empty():
            raise EmptyQueueError("empty")
        return self.items[self.front]

    def last(self):
        if self.is_empty():
            raise EmptyQueueError("empty")
        rear = (self.front + self.count - 1) % len(self.items)
        return self.items[rear]

    def display(self):
        print(self.items)

    def rezise(self, new_size):
        old_size = self.items
        self.items = [None] * new_size
        i = self.front
        for j in range(self.count):
            self.items[j] = old_size[i]
            i = (1 + i) % len(old_size)
        self.front = 0


qu = deque(6)
