for i in range(int(input())):

    arr = list(map(int,input().split()))
    l = []
    for i in range(len(arr)):
        s = abs((arr[-1] - arr[i]))
        l.append(s)
    if l[0] > l[1]:
        print('Cat B')
    elif l[0] < l[1]:
        print('Cat A')
    elif l[0] == l[1]:
        print('Mouse C')


