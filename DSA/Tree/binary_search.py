def Binary_search(l, start, end, data):
    mid = (start+end)//2

    if l[mid] == data:
        return mid
    if mid == start:
        return False

    if l[mid]>data:
         end = mid
         return Binary_search(l, start, end, data)
    else:
         start = mid
         return Binary_search(l, start, end, data)

l = [2,3,4,5,6,7,8,9,10]
print(Binary_search(l, 0, len(l), 0))
