l = [str(i) for i in range(1,10)]
i=0
while i<len(l):
    p = l[i]
    i+=1
    p+=p[-1]
    if int(p) < 10**9:
        l.append(p)

# print(l)

for _ in range(int(input())):
    n = int(input())
    c=0
    for i in l:
        if int(i)<=n:
            c+=1
    print(c)






