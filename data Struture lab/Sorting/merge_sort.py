def merge(arr1,arr2):
    print('merge',arr1,arr2)
    l=[]

    while 1:
        if arr1 == [] or arr2 == []:
            l = l+arr1+arr2
            break
        if arr1[0] > arr2[0]:
            x = arr2.pop(0)
            l.append(x)
        else:
            x = arr1.pop(0)
            l.append(x)
    return l


def sort(l):
    print('sort',l)
    if len(l) == 1:
        return l
    mid = len(l)//2
    left=l[:mid]
    r = l[mid:]
    return merge(sort(left),sort(r))
print(sort([4,7,2,3,1]))






