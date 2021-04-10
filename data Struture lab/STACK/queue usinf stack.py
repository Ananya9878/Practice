class Stack:
    def __init__(self):
        self.list = []

    def empty(self):
        return self.list == []

    def push(self,data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

    def size(self):
        return len(self.list)

    def peek(self):
        return self.list[-1]

class queue:
    def __init__(self):
        self.s1 = Stack()

    def empty(self):
        return self.s1.empty()

    def enqueue(self,data):
        self.s1.push(data)

    def dequeue(self):
        temp_st = Stack()
        while self.s1.empty() == False:
            h = self.s1.pop()
            temp_st.push(h)
        w = temp_st.pop()
        while temp_st.empty() == False:
            h = temp_st.pop()
            self.s1.push(h)
        return w

    def size(self):
        return self.s1.size()

    def rear(self):
        return self.s1.peek()

    def front(self):
        temp_st = Stack()
        while self.s1.empty() == False:
            h = self.s1.pop()
            temp_st.push(h)
        w = temp_st.peek()
        while temp_st.empty() == False:
            h = temp_st.pop()
            self.s1.push(h)
        return w
    def display(self):
        print(self.s1.list)

class new_stack:
    def __init__(self):
        self.que = queue()

    def size(self):
        return self.que.size()

    def push(self,data):
        return self.que.enqueue(data)

    def pop(self):
        for i in range(self.size()-1):
            self.que.enqueue(self.que.dequeue())
        return self.que.dequeue()

    def peek(self):
        return self.que.rear()

    def is_empty(self):
        return self.que.empty()
    def display(self):
        return self.que.display()




# q = queue()
# print('1.enqueue')
# print('2.dequeue')
# print('3 rear')
# print('4 size')
# print('5 front')
# print('6 display')
#
#
# while 1:
#     x = int(input('enter'))
#     if x==1:
#         s = int(input())
#         q.enqueue(s)
#     if x==2:
#         print(q.dequeue())
#     if x==3:
#         print(q.rear())
#     if x==4:
#         print(q.size())
#     if x==5:
#         print(q.front())
#     if x == 6:
#         (q.display())
st1 = new_stack()
print('1.push')
print('2.pop')
print('3 peek')
print('4 size')
print('5 display')



while 1:
    x = int(input('enter'))
    if x==1:
        s = int(input())
        st1.push(s)
    if x==2:
        print(st1.pop())
    if x==3:
        print(st1.peek())
    if x==4:
        print(st1.size())

    if x == 5:
        (st1.display())











