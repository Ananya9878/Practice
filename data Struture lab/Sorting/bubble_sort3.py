l=[6,2,9,1,3,4]
for j in range(len(l)):
    for i in range(len(l)-1-j):
        if l[i] > l[i+1]:
            l[i] , l[i+1] = l[i+1],l[i]
print(l)
# ///////////////////////////
# for j in range(len(l)):
#     for i in range(len(l)-1-j):
#         if l[i] > l[i+1]:
#             l[i+1] , l[i] = l[i],l[i+1]
# print(l)





