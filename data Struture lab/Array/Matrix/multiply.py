# a=2
# b=3
# c=3
# d=2
# m1 = [[1,2,3],
#      [3,4,5]
#      ]
# m2 = [[2,2],
#      [3,4],
#      [8,6]]
# m3=[[0,0],
#     [0,0],
#     ]
# for i in range(a):
#     for j in range(d):
#         for k in range(b):
#             m3[i][j] += m1[i][k]*m2[k][j]
# print(m3)
m1,n1 = 3,2
# l = [[0]*m1]*n1
l = [[0]*m1 for i in range(n1)]
l[1][1] = 1
print(l)



