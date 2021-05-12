for _ in range(int(input())):
    n = int(input())
    m = n
    c=0
    while n!=1:
        if n%6==0:
            n = n//6
            c+=1
        else:
            n = n*2
            c+=1
        if c>50:
            c = -1
            break


    print(c)
