# botton up......................................
def knap(p,w,c,i,d):
    if i == 0:
        return 0
    if c == 0:
        return 0
    if d[c][i] != -1:
        return d[c][i]
    if c>=w[i-1]:
        a = knap(p,w,c-w[i-1],i,d)+p[i-1]
    else:
        a = 0
    b = knap(p,w,c,i-1,d)
    d[c][i] = max(a,b)
    print("function cll for", c, i,max(a,b))
    return max(a,b)

profit = [5,3,3,3,3]
weight = [5,3,3,3,3]
c = 10
n = len(profit)
d = [[-1]*(n+1) for i in range(c+1)]
# g = knap(profit,weight,c,n,d)
# print(g)
# .................................................................
# TOP DOWN APPROACH

profit = [5,3,3,3,3]
weight = [5,3,3,3,3]
w = 13
n = len(profit)
dp = [[-1]*(w+1) for i in range(n+1)]
dp[0][0] = 0
for i in range(n+1):
    for j in range(w+1):
        if i==0 or j==0:
            dp[i][j] = 0
        elif j>=weight[i-1]:
            a = dp[i][j-weight[i-1]]+profit[i-1]
            b = dp[i-1][j]
            dp[i][j] = max(a,b)
        else:
            dp[i][j] = dp[i-1][j]
# print(dp)
print(dp[n][w])

