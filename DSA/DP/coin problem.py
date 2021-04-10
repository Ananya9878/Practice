a = [2,3,6]
w = 10

l = [[1000]*(w+1) for i in range(len(a)+1)]
for i in range(len(a)+1):
    for j in range(w+1):
        if j == 0:
            l[i][j] = 0
        elif j>=a[i-1]:
            x = l[i][j-a[i-1]]+1
            y = l[i-1][j]
            l[i][j] = min(x,y)
        elif j<a[i-1]:
            l[i][j] = l[i-1][j]

print(l[len(a)][w])
profit = [1,1,1]
weight = [2,3,6]
w = 12
n = len(profit)
dp = [[1000]*(w+1) for i in range(n+1)]
for i in range(n+1):
    for j in range(w+1):
        if j==0:
            dp[i][j] = 0
        elif j>=weight[i-1]:
            a = dp[i][j-weight[i-1]]+profit[i-1]
            b = dp[i-1][j]
            dp[i][j] = min(a,b)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][w])