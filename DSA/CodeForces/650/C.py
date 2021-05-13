#  submit it plsssss
for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    s = ('0'*(k))+s+('0'*(k))
    c = 0
    p = 2*k+1
    res=0
    for i in range(len(s)):
        if s[i] == '0':
            c+=1
        else:
            c = 0
        if c == p:
            res+=1
            c=k
    # if c >= k+1:
    #     res+=1

    print(res)










