for _ in range(int(input())):
    a,b = map(int,input().split())
    l1 = min(a,b)*2
    b1 = max(a,b)
    l2,b2 = b1,l1
    l = max(l1,l2)
    b = max(b1,b2)
    print(l*b)




