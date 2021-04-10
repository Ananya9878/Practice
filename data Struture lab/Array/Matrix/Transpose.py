m=3
n=3
m = [[0,2,-3],
     [-2,1,6],
     [3,-6,0]]
k=2
m1=[]
for i in range(len(m)):
    temp=[]
    for j in range(len(m[i])):
        print(m[j][i])
        temp.append((m[j][i]))

    m1.append(temp)
print(m1)
# flag = True
# for i in range(len(m)):
#     for j in range(len(m[i])):
#         # print(i,j)
#         if m[i][j] != -m[j][i]:
#             flag = False
#
#
#
# if flag:
#     print('S')
# else:
#     print('N')











