for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    a_odd,a_even = a//2,a//2
    if a & 1:
        a_odd+=1
    b_odd, b_even = b // 2, b // 2
    if b & 1:
        b_odd += 1

    print(a_odd*b_odd+a_even*b_even)








