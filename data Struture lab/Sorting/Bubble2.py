l = [1, 9, 3, 6, 7, 0, 4, 9, 5, 5]
# l = [1, 3, 6, 7, 0, 4, 9, 5, 5, 9]
# l = [1, 3, 6, 0, 4, 7, 5, 5, 9, 9]
# l = [1, 3, 0, 4, 6, 5, 5, 7, 9, 9]
# l = [1, 0, 3, 4, 5, 5, 6, 7, 9, 9]
# l = [0, 1, 3, 4, 5, 5, 6, 7, 9, 9]
# l=[5,4,3,2,1,0]
# l=[4,3,2,1,0,5]
# l=[3,2,1,0,4,5]
# l=[2,1,0,3,4,5]
# l=[1,0,2,3,4,5]
# l=[0,1,2,3,4,5]

# for i in range(len(l)):
#     for j in range(0,len(l)):
#         print(i,j)
#         if l[i]<l[j]:
#             l[i],l[j] = l[j],l[i]
#     print(i,l)
for j in range(len(l)-1):
    for i in range(1,len(l)-j):
        if l[i]<l[i-1]:
            l[i],l[i-1] = l[i-1],l[i]
    print(l)
