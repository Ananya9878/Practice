for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = [1]*n
    if len(set(arr)) == 1:
        print(1)
        print(*ans)
        continue
    for i in range(1,n):
        if arr[i-1] != arr[i]:
            if ans[i-1] == 1:
                ans[i] = 2
            else:
                ans[i] = 1
        else:
            if i == 1:
                ans[i] = 2

    if ans[0] == ans[-1]:
        if arr[0] != arr[-1]:
            if ans[-2] == 1:
                ans[-1] = 2
            else:
                if arr[-1] == arr[-2]:
                    ans[-1] = 2
                else:
                    ans[-1] = 3

    ans1 = [2] * n
    for i in range(1, n):
        if arr[i - 1] != arr[i]:
            if ans1[i - 1] == 2:
                ans1[i] = 1
            else:
                ans1[i] = 2
        else:
            if i == 1:
                ans1[i] = 1


    if ans1[0] == ans1[-1]:
        if arr[0] != arr[-1]:
            if ans1[-2] == 2:
                ans1[-1] = 1
            else:
                if arr[-1] == arr[-2]:
                    ans1[-1] = 1
                else:
                    ans1[-1] = 3

    if len(set(ans1))<len(set(ans)):
        print(len(set(ans1)))
        print(*ans1)
    else:
        print(len(set(ans)))
        print(*ans)



