for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    flag = True
    while len(l)>1:
        if flag:
            if l[-1]<=l[-2]:
                l.pop()
            else:
                flag = False

        else:
            if l[-1]>=l[-2]:
                l.pop()
            else:
                flag = True
                break
    print(len(l)-1)



