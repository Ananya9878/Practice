for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = 0
    c1=0
    for i in range(n):
        if i%2 == 0 and l[i]%2!=0:
            c+=1
        if i%2 != 0 and l[i]%2==0:
            c1+=1

    if c == c1:
        print(c)
    else:
        print(-1)

