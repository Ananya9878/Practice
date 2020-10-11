def quick(arr):
    print('quick',arr)
    if len(arr) < 2:
        return arr
    l , e ,r = [] , [] , []
    p = arr[-1]
    for i in arr:
        if i < p:
            l.append(i)
        elif i > p:
            r.append(i)
        else:
            e.append(i)
    return (quick(l) + e + quick(r))
print(quick([3,6,2,1]))
