# a = 3
# b = 2
# print(bin(a))
# print(bin(b))
# print(a & b)
# print(a | b)
# print(a ^ b)

# l=[1,6,10,11,3,4,5,6]
# for i in range(len(l)):
#     if l[i] & 1:
#         print(l[i])

# a = -1
# if a:
#     print('Hello')
# while a:
#     print(a)
#     a+=1

# a=1
# b=1
# print(a ^ b)

# import time
# def even(a):
#     if a%2 == 0:
#         x = 1
#         # print('Even')
#     else:
#         x=2
#         # print('Odd')
# def even1(a):
#     while a:
#         if a & 1 == 0:
#             x=1
#             # print('Even')
#         else:
#             x=2
#             # print('odd')
#         a-=1

# a=5100000
# t1=(time.time())
# even(a)
# t2 = time.time()
# even1(a)
# t3 = time.time()
# print(t3-t2)
# print(t2-t1)
# print(time.time())

# a=8
# # b=1
# t = (a & b) + (a | b)
# print(t)
# for i in range(a):
#     # print(i,a-i)
#     if ((i & a-i) + (i | a-i)) == a:
#         print(i,a-i)
# for i in range(int(input())):
#     a = int(input())
#     for i in range(a):
#         if ((i & a-i) + (i | a-i)) == a:
#             print(i,a-i)
#             break

for i in range(int(input())):
    a,b = map(int,input().split())
    arr = list(map(int,input().split()))
    print(max(a,b))



