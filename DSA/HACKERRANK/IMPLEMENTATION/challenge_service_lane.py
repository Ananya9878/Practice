width = list(map(int,input().split()))
cases = list(map(int,input().split()))
l1 = []
for i in cases:
    print(i)

    l = []
    for q in range(i[0], i[1] + 1):
        l.append(width[q])
    l1.append(min(l))
print l1

