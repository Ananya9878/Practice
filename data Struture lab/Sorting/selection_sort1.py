# l=[1,9,3,6,7,0,4,9,5,5]
# l=[0,9,3,6,7,1,4,9,5,5]
# l=[0,1,3,6,7,9,4,9,5,5]
# l=[0,1,3,4,7,9,6,9,5,5]
# l=[0,1,3,4,5,9,6,9,7,5]
# l=[0,1,3,4,5,5,6,9,7,9]
# l=[0,1,3,4,5,5,6,7,9,9]

def mini(arr,k):
    m = k
    for i in range(k,len(arr)):
        if arr[m]>arr[i]:
            m = i
    return m

def selection_sort(arr):
    for i in range(len(arr)-1):
        m = i
        for j in range(i, len(arr)):
            if arr[m] > arr[j]:
                m = j
        # t=mini(arr,i)
        arr[i],arr[m] = arr[m],arr[i]
    return arr


if __name__ == '__main__':
    l = [1, 9, 3, 6, 7, 0, 4, 9, 5, 5]
    print(selection_sort(l))



