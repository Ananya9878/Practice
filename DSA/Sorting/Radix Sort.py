def counting(arr,k):
    d = {}
    l=[]
    for i in arr:
        if k==0:
            t = i%10
        else:
            t = i//(10**k)
            t = t%10
        if t not in d:
            d[t] = [i]
        else:
            d[t].append(i)
    # print(d)
    for i in range(10):
        if i in d:
            l+=d[i]
    return l

def radixSort(arr):
    p=str(max(arr))
    for i in range(len(p)):
        arr = counting(arr,i)
        # print(arr)
    return arr



arr = [3,5,21,20,11,60,8,10,100]
# print(counting(arr,0))
print(radixSort(arr))

