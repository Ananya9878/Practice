# from itertools import combinations
arr=[1,2,4,5,7,8,10]
d=3
# x = list(combinations(arr,3))
c=0
# for i in x:
#     if i[1]-i[0] == i[2]-i[1] == d:
#         c+=1
# print(c)
for i in arr:
    # print(i)
    if i+d in arr and i+2*d in arr:
        c+=1
print(c)


