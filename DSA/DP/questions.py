a = [2,3,6]
w = 10

l = [[-1]*(w+1) for i in range(len(a)+1)]
l[0][0] = 0
for i in range(len(a)+1):
    for j in range(w+1):
        if i == 0 or j == 0:
            l[i][j] = 0
        elif j>=a[i-1]:
            x = l[i][j-a[i-1]]+a[i-1]
            y = l[i-1][j]
            l[i][j] = max(x,y)
        elif j<a[i-1]:
            l[i][j] = l[i-1][j]

print(l[len(a)][w])

l = [[-1]*(w+1) for i in range(len(a)+1)]
l[0][0] = 0
for i in range(len(a)+1):
    for j in range(w+1):
        if i == 0 or j == 0:
            l[i][j] = 0
        elif j>=a[i-1]:
            x = l[i-1][j-a[i-1]]+a[i-1]
            y = l[i-1][j]
            l[i][j] = max(x,y)
        elif j<a[i-1]:
            l[i][j] = l[i-1][j]

print(l[len(a)][w])



