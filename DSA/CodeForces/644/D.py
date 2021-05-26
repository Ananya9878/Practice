for _ in range(int(input())):
    n,k = map(int,input().split())
    if n <= k:
        ans = 1
        print(ans)
        continue
    elif k == 1:
        ans = n
        print(ans)
        continue
    t = int(n**(0.5))
    t = min(t+1,k)
    ans = n
    for i in range(t,0,-1):
        if n % i == 0:
            x = n // i
            if x<=k:
                ans = min(ans,i)
            else:
                ans = min(ans,x)
    print(ans)
            # if x > k:
            #     print(x)
            # else:
            #     print(i)
            # break






'''  
n=8 k =7
t = 3
x = 8

'''






