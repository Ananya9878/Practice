for _ in range(int(input())):
    s = input()
    l = []
    c=0
    for i in s:
        if i == 'L':
            c+=1
        else:
            l.append(c)
            c=0
    l.append(c)
    print(max(l)+1)
