for _ in range(int(input())):
    n1,n2 = map(int,input().split())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    l1.sort()
    l2.sort()
    c = 0
    i = 0
    j = len(l2)-1
    while 1:
        a = sum(l1)
        b = sum(l2)
        if a>b:
            break
        if i == len(l1) or j == -1:
            c = -1
            break
        if l2[j]>l1[i]:
            l1[i],l2[j] = l2[j],l1[i]
            c+=1
        i+=1
        j-=1

    if sum(l1) == sum(l2):
        c = -1

    print(c)





