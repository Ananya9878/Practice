for _ in range(int(input())):
    a,b,k = map(int,input().split())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))

    d1,d2 = {},{}
    for i in l1:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i]+=1
    for i in l2:
        if i not in d2:
            d2[i] = 1
        else:
            d2[i]+=1

    c=0
    for i in range(k):
        p = (l1[i],l2[i])
        t = k-(d1[l1[i]])-(d2[l2[i]])+1
        c+=t
    print(c//2)

