mat=[[2,0,0],
     [0,2,0],
     [0,0,2]]
a=3
b=3
flag = True
# l=mat[0][0]
for i in range(a):
    if mat[i][i] != 0:
        flag = False
if flag:
    print('t')
else:
    print('F')
