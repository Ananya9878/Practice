for _ in range(int(input())):
    n = int(input())
    l=[]
    f1=0
    f2=1
    f=f1+f2
    while 1:
        f=f1+f2
        f1=f2
        f2=f
        if f>n:
            break
        if f%2==0:
            l.append(f)
    print(sum(l))




