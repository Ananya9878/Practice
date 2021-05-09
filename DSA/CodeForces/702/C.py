cube = 10**4
s = set()
l = []

for i in range(1,cube+1):
    s.add(i**3)
    l.append(i**3)

for _ in range(int(input())):
    n = int(input())
    flag = True
    for i in l:
        h = n-i
        if h in s:
            print('YES')
            flag = False
            break
    if flag:
        print('NO')





