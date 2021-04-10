for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    m = n//2
    r = l.count(-1)
    bot,accepted,slow=0,0,0
    for i in l:
        if i==0 or i==1:
            bot+=1
        if i>k:
            slow+=1
        if i<k:
            accepted+=1
    if r > m:
        print('Rejected')
    elif bot == n:
        print('Bot')
    elif slow>0:
        print('Too Slow')
    else:
        print('Accepted')

