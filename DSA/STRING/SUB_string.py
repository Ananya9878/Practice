s = ')()()('
l = []
# res=0
c=0
for i in range(len(s)):
    for j in range(0,len(s)-i):
        l.append(s[j:j+i+1])
# print(l)
for j in range(len(l)):
    s1 = l[j]
    res=0

    for i in range(len(s1)):
        if s1[i] == '(':
            res+=1
        else:
            res-=1
        if res < 0:
            break
    if res == 0:
        c+=1
print(c)






