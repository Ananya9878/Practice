l=[5,3,2,8,9,1,0]

def merge(arr1,arr2):
    arr3 = []
    while len(arr1)>0 and len(arr2)>0:
        if arr1[0]<arr2[0]:
            arr3.append(arr1.pop(0))
        else:
            arr3.append(arr2.pop(0))

    arr3+=arr1+arr2
    return arr3



def sort(l):
    if len(l)==1:
        return l
    t = len(l)//2
    l1=l[:t]
    l2=l[t:]
    return merge(sort(l1),sort(l2))

print(sort(l))






