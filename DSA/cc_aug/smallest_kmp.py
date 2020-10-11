for _ in range(int(input())):
    s1 = input()
    s2 = input()
    r = list(s2)
    s1 = list(s1)
    for i in range(len(s2)):
        s1.remove(r[i])
    s1.sort()
    flag = 0
    for i in range(len(s1)):
        if s1[i] > s2[0]:
            s1[i] = s2+s1[i]
            # s3[i]+=s2
            break
    d = ''.join(s1)
    # d2 = ''.join(s3)
    print(d)









