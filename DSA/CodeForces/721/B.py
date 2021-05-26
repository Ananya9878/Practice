for _ in range(int(input())):
    n = int(input())
    s = input()
    s = list(s)
    a,b = 0,0
    

    # for i in range(n):
    #     if flag:
    #         if s == s[::-1]:
    #             if s[i] == '0':
    #                 s[i] = '1'
    #                 a+=1
    #                 flag1 = True
    #         else:
    #             if flag1:
    #                 # s = s[::-1]
    #                 flag1 = False
    #             else:
    #                 if s[i] == '0':
    #                     s[i] = '1'
    #                     a+=1
    #                     flag1 = True
    #
    #         flag = False
    #     else:
    #         if s == s[::-1]:
    #             if s[i] == '0':
    #                 s[i] = '1'
    #                 b += 1
    #                 flag1 = True
    #         else:
    #             if flag1:
    #                 # s = s[::-1]
    #                 flag1 = False
    #             else:
    #                 if s[i] == '0':
    #                     s[i] = '1'
    #                     b+=1
    #                     flag1 = True
    #
    #         flag = True
    # print(a,b,s)
    if a>b:
        print('BOB')
    elif a<b:
        print('ALICE')
    if a == b:
        print('DRAW')