def insert(heap,data):
    for i in range(len(heap)):
        if heap[i] == None:
            heap[i] = data
            p=i+1
            break
    while 1:

        new_p = p//2
        if new_p == 0:
            break
        if heap[p-1] > heap[new_p-1]:
            heap[p-1],heap[new_p-1] = heap[new_p-1],heap[p-1]
        else:
            break
        p = new_p
        print(heap)



# heap = [None]*20

heap = []
#
# insert(heap,12)
# insert(heap,18)
# insert(heap,9)
# insert(heap,90)
# insert(heap,99)

def insert1(heap,data):
    heap.append(data)
    p = len(heap)

    while 1:
        k = p//2
        if k == 0:
            break
        if heap[p-1] > heap[k-1]:
            heap[p-1],heap[k-1] = heap[k-1],heap[p-1]
        else:
            break
        p = k
    # print(heap)

def delete(heap):
    t = heap[0]
    heap[0],heap[-1] = heap[-1],heap[0]
    parent = 1
    while 1:
        left_child = 2*parent
        right_child = 2*parent+1
        if left_child>len(heap) or right_child>len(heap):
            break
        if heap[left_child-1]>heap[right_child-1]:
            if heap[left_child-1] > heap[parent-1]:
                heap[left_child-1],heap[parent-1] = heap[parent-1],heap[left_child-1]
                parent = left_child
            else:
                break
        else:
            if heap[right_child-1] > heap[parent-1]:
                heap[right_child-1],heap[parent-1] = heap[parent-1],heap[right_child-1]
                parent = right_child
            else:
                break
    return heap.pop()









a = [10,8,7,5,4,3]
for i in a:
    insert1(heap,i)


# print(heap)
t=delete(heap)
print(t,heap)
# insert1(heap,6)
insert1(heap,10)
# insert1(heap,6)
# insert1(heap,6)
print(heap)
print(delete(heap))





