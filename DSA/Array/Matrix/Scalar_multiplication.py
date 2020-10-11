m=3
n=3
m1 = [[0,2,-3],
     [-2,1,6],
     [3,-6,0]]
k=2
for i in range(m):
    for j in range(n):
        m1[i][j] *=k 
print(m1)
