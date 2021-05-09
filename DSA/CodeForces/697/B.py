# Code for B
c,d = 0,0
a = 0
b = 0
l1 = [0]
l2 = set([0])

while a<10**6:
    a+=2020
    l1.append(a)
while b<10**6:
    b+=2021
    l2.add(b)

for _ in range(int(input())):
    n = int(input())
    x,y = 1,1
    flag = True
    for i in l1:
        k = n-i
        if k in l2:
            print('YES')
            flag = False
            break
    if flag:
        print('NO')







