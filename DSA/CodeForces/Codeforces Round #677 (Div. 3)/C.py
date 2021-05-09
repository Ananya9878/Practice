for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    m = max(l)
    if len(set(l)) == 1:
        print(-1)
    else:
        for i in range(n):
            if l[i] == m:
                if i>0 and l[i-1] < m:
                    print(i+1)
                    break
                if i<n-1 and l[i+1]<m:
                    print(i+1)
                    break

# 6
# 5
# 5 3 4 4 5
# 3
# 1 1 1
# 5
# 4 4 3 4 4
# 5
# 5 5 4 3 2
# 3
# 1 1 2
# 5
# 5 4 3 5 5






