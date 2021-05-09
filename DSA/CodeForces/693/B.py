for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    s = sum(l)
    if s&1:
        print('NO')
        continue
    d = {1:0,2:0}
    flag = True
    for i in l:
        d[i]+=1
    x,y = 0,0
    while d[2]>=y:
        x = s//2 - (2 * y)
        y+=1
        if x<0:
            break
        if x>=0 and x<=d[1]:
            print('YES')
            flag = False
            break
    if flag:
        print('NO')












'''
1 1 2  
'''