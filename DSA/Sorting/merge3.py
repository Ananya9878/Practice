l=[4,7,8,9,3,2,1,0]
def merge(arr1,arr2):
    arr3=[]
    while len(arr1)>0 and len(arr2)>0:
        if arr1[0]<arr2[0]:
            arr3.append(arr1.pop(0))
        else:
            arr3.append(arr2.pop(0))

    arr3+=arr1+arr2
    return arr3

def sort(arr):
    if len(arr) <= 1:
        return arr
    t = len(arr)//2
    l1=arr[:t]
    l2=arr[t:]
    return merge(sort(l1),sort(l2))

print(sort(l))
l1=[4,7,8,9]
l2=[3,2,1,0]
l1=[4,7]
l2=[8,9]
l2=[4]
l2=[7]



