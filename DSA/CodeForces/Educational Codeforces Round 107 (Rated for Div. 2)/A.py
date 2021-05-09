for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    c,d = arr.count(1),arr.count(3)

    # l,dl = 0,0
    # while n>0:
    #     a = arr.pop(0)
    #     if a == 1:
    #         l+=1
    #     elif a==2:
    #         dl+=1
    #     else:
    #         if dl>l:
    #             dl+=1
    #         else:
    #             l+=1
    #     n-=1

    print(c+d)