n=int(input())
arr = list(map(int,input().split()))
l1=[len(arr)]
while 1:
    l=[]
    for i in range(len(arr)):
        q = min(arr)
        s = arr[i] - q
        if s != 0:
            l.append(s)
    if len(l) == 0:
        break
    l1.append(len(l))
    arr = l
print(l1)

# for i in range(len(l)):
#     q = min(l)
#     s = l[i] - q
#     if s!=0:
#         l.append(s)
#         l1.append(len(l))
# print(l1)








