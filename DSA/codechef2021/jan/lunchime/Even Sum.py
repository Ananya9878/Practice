for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    e,o = 0,0
    for i in l:
        if i&1:
            o+=1
        else:
            e+=1

    if o&1==0:
        print('1')
    else:
        print('2')