# NON REPETED
# arr = [3,4,4,3]
# w = 10
# c = 0
# k = [[0]*(w+1) for i in range(len(arr)+1)]
# for i in range(len(arr)+1):
#     for j in range(w+1):
#         if j==0:
#             k[i][j] = 1
#         elif j>=arr[i-1]:
#             a = k[i-1][j-arr[i-1]]
#             b = k[i-1][j]
#             k[i][j] = a+b
#         else:
#             k[i][j] = k[i-1][j]
#
# for i in k:
#     print(i)
# ..........REPETED
arr = [3,4]
w = 10
c = 0
k = [[0]*(w+1) for i in range(len(arr)+1)]
for i in range(len(arr)+1):
    for j in range(w+1):
        if j==0:
            k[i][j] = 1
        elif j>=arr[i-1]:
            a = k[i][j-arr[i-1]]
            b = k[i-1][j]
            k[i][j] = a+b
        else:
            k[i][j] = k[i-1][j]

for i in k:
    print(i)



