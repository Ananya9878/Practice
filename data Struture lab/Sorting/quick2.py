l = [1, 9, 3, 6, 7, 0, 4, 9, 5, 5]
def sort(arr):
    print('sort calling for',arr)
    if len(arr) <= 1:
        return arr
    p=arr[-1]
    l,e,r = [],[],[]
    for i in arr:
        if i>p:
            r.append(i)
        elif i<p:
            l.append(i)
        else:
            e.append(i)
    return sort(l)+e+sort(r)


print(sort(l))


