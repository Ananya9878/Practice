for _ in range(int(input())):
    a = int(input())
    l=[]
    for i in range(a):
        if i%3 == 0 or i%5==0:
            l.append(i)
    print(sum(l))


