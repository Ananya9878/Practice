profit = [5,3,3,3,3]
weight = [5,3,3,3,3]
w = 8
n = len(profit)
dp = [[-1]*(w+1) for i in range(n+1)]
dp[0][0] = 0
for i in range(n+1):
    for j in range(w+1):
        if i==0 or j==0:
            dp[i][j] = 0
        elif j>=weight[i-1]:
            a = dp[i-1][j-weight[i-1]]+profit[i-1]
            b = dp[i-1][j]
            dp[i][j] = max(a,b)
        else:
            dp[i][j] = dp[i-1][j]
print(dp)
print(dp[n][w])





