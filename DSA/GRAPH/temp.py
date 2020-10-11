# l=[1,5,2,3,4,5,5,5,6]
# # for i in range(len(l)):
# print(l[4])
#     # print(i,l[i])
# k=[(1,0),(2,0),(3,1)]
# conn =[(2,1)]
# for i in range(len(conn)):
#     print(i)

# for i in k:
#     print(i)
#     if i[0] == 2:
#         print('y')
# def min_weight(p):
#     # p = [(1,2),(2,3),(3,1)]
#     min_index = 0
#     for i in range(len(p)):
#         if p[i][-1] < p[min_index][-1]:
#             min_index = i
#     # print(p[min_index])
#     a = p.pop(min_index)
#     return a
# p = [(1,2),(2,3),(3,1)]
# print(min_weight(p))
# print(p)
# f = open('input.txt','r')
# for i in range(4):
#     a, b, c = map(int, f.readline().split())
#     print(a,b,c)
# l=[1,3,4,5,6,8,9,10,12]
# k = 0
# a=-1
# b=len(l)
# while 1:
#
#     c = (a+b)//2
#     if l[c] > k:
#         b = c
#     elif l[c] < k:
#         a = c
#     else:
#         print('True')
#         break
#     if a+1 ==  b:
#         print('False')
#         l.insert(b,k)
#         break
#
# print(l)
# p=[(1,0)]
# k = p[0][0]
# p=[[(1,1),(1,1)],[(1,0),(2,0)]]
# m=0
# for i in range(len(p)):
#     if p[i][-1][-1]< p[m][-1][-1]:
#         m = i
#     # print(m)
# k = p.pop(m)
# print(k)
# print(p)
# def mini(p):
#     k = 0
#     for i in range(len(p)):
#         # print(i)
#         if p[i][-1][-1] < p[k][-1][-1]:
#             k = i
#     return p.pop(k)

# p = [[(1,0),(2,1)],[(1,0),(3,0)]]
# print(p[-1][-1])
# print(mini(p))
# q = [(1,0),(3,0)]
# k = q[-1][0]
# print(k)
l=[5,4,1,2]
# mini = l[0]
# for i in range(len(l)):
#     if l[i] < mini:
#         mini = l[i]
#         k = i
# print(mini,k)
if l == sorted(l):
    print('y')
else:
    print('n')

