class MaxHeap:
    def __init__(self):
        self.heap = [None]*45
        self.top = 0

    def insert(self,data):
        self.top+=1
        if self.top > len(self.heap):
            self.heap+=[None]*len(self.heap)
        self.heap[self.top-1] = data

        p = self.top
        while p>0:

            new_p = p//2
            if new_p<=0:
                break
            if self.heap[new_p-1] < self.heap[p-1]:
                self.heap[new_p-1],self.heap[p-1] = self.heap[p-1],self.heap[new_p-1]
            else:
                break

            p = new_p
        # self.top+=1

    def ExtractMax(self):
        self.heap[self.top-1],self.heap[0] = self.heap[0],self.heap[self.top-1]
        # print(self.heap)
        r = 0
        while 1:
            lc = 2*r+1
            rc = 2*r+2
            max_index = r
            if self.heap[lc] is not None:
                if self.heap[lc] > self.heap[max_index]:
                    max_index = lc
            if self.heap[rc] is not None:
                if self.heap[rc] > self.heap[max_index]:
                    max_index = rc
            if max_index != r:
                self.heap[max_index],self.heap[r] = self.heap[r],self.heap[max_index]
            else:
                break
            r = max_index
        k = self.heap[self.top-1]
        self.heap[self.top-1] = None
        self.top-=1
        return k

    def get_max(self):
        return self.heap[0]




t = [13,9,10,8,6,5,4,3]
H = MaxHeap()
for i in t:
    H.insert(i)
print(H.heap)
print(H.ExtractMax())
print(H.ExtractMax())
print(H.heap)




