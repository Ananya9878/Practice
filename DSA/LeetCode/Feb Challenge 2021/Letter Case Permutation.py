S = "a1b2"
a = S.lower()
v = S.upper()
l = [a,v]
flag = False
res = ''
while len(l)!=4:
    for i in S:
        if i.isalpha():
            if flag == False:
                res+=i.lower()
                flag = True
            else:
                res+=i.upper()
                flag = False
        else:
            res+=i
    if res not in l:
        l.append(res)
    res = ''
    print(l)





