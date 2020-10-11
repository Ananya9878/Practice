s = '99100'
flag = False
for i in range(1,len(s)):
    x = int(s[:i])
    v = x
    s1 = s[i:]
    # print(x,s1)
    while len(s1)>0:
        x+=1
        # print(x,s1)
        a = str(x)
        if a == s1[:len(a)]:
            s1 = s1[len(a):]
        else:
            break
    if len(s1) == 0:
        print('Yes', v )
        flag = True
        break
if flag == False:
    print('No')
