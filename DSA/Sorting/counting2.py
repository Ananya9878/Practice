l = [1, 9,0,0, 3, 6, 7, 0, 4, 9,1, 5, 5]
arr = [0]*10

for i in l:
    arr[i]+=1
print(arr)
l=[]
for i in range(len(arr)):
    l+=[i]*arr[i]
    # print(i,arr[i],l)
    print(l)


