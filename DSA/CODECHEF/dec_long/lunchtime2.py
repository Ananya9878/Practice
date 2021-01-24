for _ in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()
    if s1 == s2:
        print('Yes')
    else:
        a = s1.count('1')
        b = s2.count('1')
        if a != b:
            print('No')
        else:
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    if s1[i] == '0':
                        print('No')
                        break
                    elif s1[i] == '1':
                        print('Yes')
                        break




