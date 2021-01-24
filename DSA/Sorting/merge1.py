l = [1, 9, 3, 6, 7, 0, 4, 9, 5, 5]

def merge(arr1,arr2):
    print('merge function',arr1,arr2)
    arr3=[]
    while len(arr1)>0 and len(arr2)>0:
        if arr1[0]<arr2[0]:
            p=arr1.pop(0)
            arr3.append(p)
        else:
            p=arr2.pop(0)
            arr3.append(p)
    arr3+=arr1+arr2
    return arr3
    # print(arr3)

def sort(arr):
    print('sort function calling:',arr)
    if len(arr) == 1:
        return arr
    t=len(arr)//2
    l1=arr[:t]
    l2=arr[t:]
    return merge(sort(l1),sort(l2))



# merge([1,2,3],[5,4,6])
print(sort(l))
