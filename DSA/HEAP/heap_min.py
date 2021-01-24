class Heap:
    def __init__(self):
        self.heap = [None]*20
        self.top = 0

    def insert(self,data):
        self.top+=1
        if self.top > len(self.heap):
            self.heap+=[None]*len(self.heap)
        self.heap[self.top-1] = data

        p = self.top
        while p>0:
            parent = p//2
            if parent<=0:
                break
            if self.heap[parent-1] > self.heap[p-1]:
                self.heap[parent-1],self.heap[p-1] = self.heap[p-1],self.heap[parent-1]
            else:
                break

            p = parent



    def Extract_Min(self):
        self.heap[self.top-1] ,self.heap[0] = self.heap[0] ,self.heap[self.top-1]
        k = self.heap[self.top - 1]
        self.heap[self.top - 1] = None
        self.top -= 1

        p = 0
        while 1:
            l = 2*p+1
            r = 2*p+2

            mini = p
            if self.heap[l] is not None:
                if self.heap[l] < self.heap[mini]:
                    mini = l

            if self.heap[r] is not None:
                if self.heap[r] < self.heap[mini]:
                    mini = r

            if mini != p:
                self.heap[mini], self.heap[p] = self.heap[p],self.heap[mini]
            else:
                break

            p = mini

        return k

H = Heap()
arr = [15,12,8,9,2,4,20]
for i in arr:
    H.insert(i)
print(H.heap)
l=[]
for i in range(len(arr)):
    k = H.Extract_Min()
    arr[i]=k
print(arr)
