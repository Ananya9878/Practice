for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = {}
    if n == 1:
        print(0)
        continue
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1

    res = 0
    maxi,mini = 0,1000000
    a,b = 0,0
    for i in d:
        if d[i]>maxi:
            maxi = d[i]
            a = i
    

    left = d[a]
    right = len(d)-1
    if left>right:
        left-=1
        right+=1
    print(min(left,right))






