def change(mat,a,b):
    if mat[a][b] == 9:
        mat[a][b] = 1
    else:
        mat[a][b]+=1
    return mat
for _ in range(int(input())):
    mat = []
    for i in range(9):
        s = input()
        mat.append(list(map(int,list(s))))


    change(mat,0,0)
    change(mat,1,3)
    change(mat,2,6)
    change(mat,3,1)
    change(mat,4,4)
    change(mat,5,7)
    change(mat,6,2)
    change(mat,7,5)
    change(mat,8,8)



    for i in mat:
        p = map(str,list(i))
        print(''.join(p))



