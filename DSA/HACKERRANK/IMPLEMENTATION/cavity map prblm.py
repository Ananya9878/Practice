n = [[9,8,9],
[1,9,1],
[1,1,1]]
for i in range(1,len(n)-1):

        n[i] = list(n[i])
        for k in range(1,len(n[i])-1):
            if n[i][k-1]< n[i][k] and n[i][k+1] < n[i][k] and n[i-1][k]< n[i][k] and n[i+1][k] < n[i][k]:
                n[i][k] = 'X'
        n[i] = ''.join(n[i])

print((n))
