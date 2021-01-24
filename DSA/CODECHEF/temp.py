# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     l=[]
#     c=0
#     for i in range(n):
#         for j in range(i+1,n):
#             t = arr[i] ^ arr[j]
#             if t > arr[i] and t > arr[j]:
#                 c+=1
#     print(c)

# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     l=[]
#     for i in range(n):
#         t=n/arr[i]
#         if t == int(t):
#             l.append(int(t))
#         else:
#             l.append(int(t+1))
#     print(max(l))

# import math
# print(math.log(9,2))
# for _ in range(int(input())):
#     x,y = map(int,input().split())
#     if y > x:
#         t = y-x
#         if t & 1:
#             print(1)
#         elif t & 1 == 0:
#             if t//2 & 1:
#                 print(2)
#             else:
#                 print(3)
#     elif x>y:
#         t = abs(x) - abs(y)
#         if t & 1 == 0:
#             print(1)
#         else:
#             print(2)

def fun(a):
    p=[]
    l = []
    for i in range(len(a)-1):
        l.append(a[i]+a[i+1])
    return l

a=[4,7,3,6,7]
while len(a)>1:
    a = fun(a)
    print(a)









