t= int(input())
for i in range(t):
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    c = 0
    for i in range(n):

        if a[i]<=0:
            c+=1
            # print(c)
    if k>c:
        print('YES')
    else:
        print('NO')
