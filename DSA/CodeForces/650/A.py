for _ in range(int(input())):
    s = input()
    p,q = s[0],s[-1]
    for i in range(1,len(s)-1,2):
        p+=s[i]
    print(p+q)

