for _ in range(int(input())):
    w,h,n = map(int,input().split())
    c=1
    if w&1 and h&1 and n>1:
        print('NO')
        continue
    elif w&1 and h&1 and n==1:
        print('YES')
        continue
    else:
        if w&1==0 and h&1==0:
            while h&1==0:
                h = h//2
                c*=2
            while w&1==0:
                w = w//2
                c*=2
        elif h&1==0:
            while h&1==0:
                h = h//2
                c*=2
        elif w&1==0:
            while w&1==0:
                w = w//2
                c*=2



    if c>=n:
        print('YES')
    else:
        print('NO')
'''
8 
4,4
2,2 2,2
1,1,1,1, 1,1,1,1
 
'''