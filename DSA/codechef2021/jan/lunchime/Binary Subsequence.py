for _ in range(int(input())):
    n = int(input())
    s = input()
    l=[]
    c0,c1=0,0
    for i in range(n):
        if s[i]=='0':
            c0+=1
        else:
            c1+=1
        if c0>c1:
            l.append(c1)
            c1,c0 = 0,0
    print(sum(l)+c0)
