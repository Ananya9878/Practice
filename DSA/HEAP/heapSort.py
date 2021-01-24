arr=[8,2,4,90,1,5,6,3]
def heapify(heap,n,i):
    max_i = i
    lr = 2*i+1
    rr = 2*i+2
    if lr<n:
        if heap[lr]>heap[max_i]:
            max_i = lr
    if rr<n:
        if heap[rr]>heap[max_i]:
            max_i = rr
    if max_i != i:
        heap[max_i],heap[i] = heap[i],heap[max_i]
        i = max_i
        heap=heapify(heap,n,i)
        return heap
    else:
        return heap


def buildHeap(arr,n):
    for i in range(n//2,-1,-1):
        arr=heapify(arr,n,i)
        # print(arr,i)
    return arr



def heapSort(arr,n):
    heap = buildHeap(arr,n)
    for i in range(n):
        heap[0],heap[n-1-i] = heap[n-1-i],heap[0]
        print(heap)
        heap = heapify(heap,n-1-i,0)
        print(heap,'****')















# print(buildHeap(arr,len(arr)))
heapSort(arr,len(arr))






