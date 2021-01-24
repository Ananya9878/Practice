def find(a):
    l = 'abcdefghijklmnop'
    for i in range(4):
        l1 = l[:len(l) // 2]
        l2 = l[len(l) // 2:]
        if a[i] == '0':
            l = l1
        else:
            l = l2
    return l
for _ in range(int(input())):
    n = int(input())
    s = input()
    res = ''
    for i in range(0,n,4):
        t = s[i:i+4]
        res+=find(t)
    print(res)








