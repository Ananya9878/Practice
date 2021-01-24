# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# a = [None]*10
# root = int(input('Enter ROOT'))
def insert(heap,value):
    # print(heap)

    for i in range(len(heap)):
        if len(heap) < 2 * (i + 1):
            heap += [None] * (2 * i+1)
        if heap[i] is None:
            heap[i] = value
            break
    while i>=0:
        p = i//2
        if heap[p] < heap[i]:
            heap[p],heap[i] = heap[i],heap[p]
            i = p
        else:
            break
    # print(heap)

    return heap

def extract_max(heap):
    max_value = heap[0]
    p = 1

    while heap[p-1] != None:
        l = 2 * p
        r = 2 * p + 1
        if heap[l-1] is None and heap[r-1] is None:
            heap[p-1] = None
            return heap
        if heap[l-1]>heap[r-1]:
            heap[p-1] = heap[l-1]
            p = l
        else:
            heap[p-1] = heap[r-1]
            p = r

    return heap,max_value




if __name__=="__main__":
    heap = [None]
    l = [5,3,67,40,44,5,47,100,50,250]
    for i in range(len(l)):
        heap = insert(heap,l[i])
    print(heap)
    arr = []
    for i in range(len(l)):
        heap,max = extract_max(heap)
        arr.append(max)
    print(arr)
    exit()
    print('1 Insert')
    print('2 Extract max')

    while 1:
        option = int(input('enter option'))
        if option == 1:
            v = int(input('enter data'))
            heap = insert(heap,v)
            print(heap)
        elif option == 2:
            heap,max_value = extract_max(heap)
            print(heap)
        else:
            break

