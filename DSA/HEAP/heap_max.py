def insert(heap,data):
    heap.append(data)
    child_index = len(heap)
    # print(child_index)
    while child_index>1:
        parent_index = child_index//2
        if heap[parent_index-1]<heap[child_index-1]:
            # print(heap[parent_index-1],heap[child_index-1])
            heap[parent_index-1],heap[child_index-1] = heap[child_index-1],heap[parent_index-1]
            # print(heap[parent_index-1],heap[child_index-1])
        else:
            break
        child_index = parent_index
    return heap


def extract_max(heap):
    value = heap[0]
    heap[0] = heap.pop()
    # print(heap)
    parent_index = 1
    while 1:
        
        left_child = 2*parent_index
        right_child = 2*parent_index+1
        if left_child>len(heap) and right_child>len(heap):
            # print(1)
            break
        elif right_child>len(heap):
            if heap[parent_index-1]<heap[left_child-1]:
                heap[parent_index-1],heap[left_child-1] = heap[left_child-1],heap[parent_index-1]
                parent_index = left_child
            else:
                break
        else:
            if (heap[parent_index-1] >= heap[left_child-1]) and heap[parent_index-1]>= heap[right_child-1]:
                # print(3)
                break
            else:
                if heap[left_child-1]>heap[right_child-1]:
                    heap[parent_index-1],heap[left_child-1] = heap[left_child-1],heap[parent_index-1]
                    parent_index = left_child
                else:
                    heap[parent_index - 1], heap[right_child - 1] = heap[right_child - 1], heap[parent_index-1]
                    parent_index = right_child

    return value

def main():
    arr = [1,2,3,4,5,6]
    heap = []
    for i in arr:
        heap=insert(heap,i)
        print(heap[0])
    print(heap)
    print(extract_max(heap))
    print(heap)


if __name__ == '__main__':
    main()
     