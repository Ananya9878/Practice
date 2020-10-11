#
# # arr = []
# # n = int(input())
# # for i in range(n):
# #     arr.append(int(input())
# #
# #     print(reversed(arr))
# # from itertools import product
# # k , m = map(int,input().split(" "))
# # arr = (" ".join(input().split(" ")))
# # input()
# # step = int(input())
# # l1=[])
# # for i in range(k):
# #     l = (list(map(int, input().split())))[1:]
# #     l1.append(l)
# # arr = map(lambda  x:sum(i*i for i in x)%m,product(*l1))
# # print(max(arr)
# # from itertools import permutations
# # s, i =(input().split())
# # z= sorted(s)
#
# # t = ('a', 'c')
# # print(t[0]+t[1])
# # p = list(permutations(z, 2))
#
# # for c in p:  # iterates through each tuple
# #     print(*p, sep = '\n')for item in c:  # iterates through each tuple items
# #         print(str(item+item+1))
# # # print(*p)
# # for i  in p:
# #     w =i[0]+i[1]
# # #     print(w)
# n= int(in

# l1=[]
# for i in range(1, n*n+1):
#     l1.append(i)
# # print(l1)
# mat=[]
# for i in range(n):
#     start = i*n
#     end = i*n+n
#     mat.append(l1[start:end])
# # print(mat)
# for i in range(len(mat)):
#     if i%2!=0:
#         print(*mat[i][::-1])
#     else:
#         print(*mat[i])
# p=0
# n=0
# z=0
# arr = list(map(int, input().split()))
# l=len(arr)
# for i in range(l):
#     if arr[i] > 0:
#         p+=1
#     elif arr[i] < 0:
#         n+=1
#     else:
# p=int(input())
# k=2*n-2
#
# for i in range(0,n):
#     for j in range(0,k):
#         print(end='')
#     k=k-2
#     for j in range(0,i+1):
#         print('*', end=' ')
#     print()




#         z+=1
# # print(p,n,z)
# s1 = p/l
# s2 = n/l
# s3 = z/l
# print('%.6f'%s1)
# print('%.6f'%s2)
# print('%.6f'%s3)




#
#
#
#
# # print()
#
#
#
#
# # q = (x**2+y**2+z**2)
# # print(q)
# #
#
# # print("".join(map(str,arr)))
# # arr1 = arr[ step :] + arr[ : step ]
# # print(*arr1)
#
# # def isValidBST(root, min=None, max=None) {
# # if (!root):
# #     return true;
# #         if (min != NULL && root->val <= min->val) return false;
# #         if (max != NULL && root->val >= max->val) return false;
# #         return isValidBST(root->left, min, root) && isValidBST(root->right, root, max);
# # s= input()
# # p = int(input())
# # l = []
# # for i in s(p):
# #     l.append(i)
# # print(*l)
# import string
# # s = input().split()
# # z=s.capitalize()
# # print(z)
# # from itertools import permutations
# # # s = input()
# # print [''.join(p) for p in permutations(input())]
#
#
# #
# # for _ in range(int(input())):
# #     loss = []
# #     N,K = map(int, input().split())
# #     p = list(map(int, input().split()))
# #     for i in range(N):
# #
# #         if p[i]>K:
# #             z = p[i]-K
# #             loss.append(z)
# #     print(sum(loss))
# # def count_string(sub_string, strings):
# #     # for _ in range(int(input())):
# #         strings=input()
# #         c=0
# #         for i in range(len(string)):
# #             if sub_string in strings[i: i+len(sub_string)]:
# #                 c+=1
# #         return c
# import re
#
# # Initialising string
# ini_str = "ababababa"
# sub_str = 'ab'
#
# # Count count of substrings using re.findall
# res = len(re.findall('(?= aba)', ini_str))
#
# # Printing result
# print("Number of substrings", res)
# string = "xyxyxxx"
#
# print(string.count("xy"))
# for _ in range(int(input())):
#     s=input()
#     c=0
#     l=['xy','yx']
s='[({)}]'
l1=[]
l2=[]
a=len(s)//2
# for i in range(len(s)):
#     if s[i] == '[':
#         l1.append(s[i])
#
#     elif s[i] == '(':
#         l1.append(s[i])
#
#     elif s[i] == '{':
#         l1.append(s[i])
#     if s[i] == ']':
#         l2.append(s[i])
#
#     elif s[i] == ')':
#         l2.append(s[i])
#
#     elif s[i] == '}':
#         l2.append(s[i])
# print(*l1)
# print(*l2)

if s[a] == s[a+1] or '}' or '{':
    print('y')
elif s[a] == ')' or '(':
    print('y')
elif s[a] == ']' or '[':
    print('y')
else:
    print('no')
# for j in range(len(l1)):















#     for i in l:
#
#         c=c+1
#     print(c)


# for _ in range(int(input())):
#     s=input()
#     c=0
#     i=1
#     while i <len(s):
#         if s[i]!=s[i-1]:
#             c+=1
#             i+=2
#         i+=1
#
#     print(c)
# for _ in range(int(input())):
#     ts = int(input())
#     while (ts%2) == 0:
#         ts=ts//2
#
#
#     print(ts//2)
#
# s= input()
# c=0
# i=1
# while i <len(s):
#     if s[i] == s[i-1]:
#         c+=1
#         i+=1
#     i+=1
# # print(c)
# for _ in range(int(input())):
#     var5 = 0
#     var10 = 0
# i=0
#
# n = input()
# if n == 'G':
#     print('C')
# elif n=='C':
#     print('G')
# elif n=='A':
#     print('U')
# elif n=='T':
#     print('A')
# else:
#     print('Invalid Input')
# def factorial(Y):
#
#     if Y == 1 or Y == 0:
#         return 1
#
#     result = 1 # variable to hold the result
#
#     for x in range(1, Y + 1, 1):
#         result *= x
#     return result
# # from math import factorial
# X, Y = map(int, input().split())
# z = X**(factorial(Y))%10
# # q = (X**z)%10
# # s = q%10
# print(z)

# i+=1

# def fizzBuzz(n):
#     n = list(map(int, input().split()))
#     for i in range(n):
#         if n % 3 == 0 and n % 5 == 0:
#             print('FizzBuzz')
#         elif n % 3 == 0 and n % 5 != 0:
#             print('Fizz')
#         elif n % 5 == 0 and n % 3 != 0:
#             print('Buzz')
#         elif n % 3 != 0 and n % 5 != 0:
#             print(n)

#
    # N = int(input())
    # arr = list(map(int, input().split()))
    #
    #
    # for i in range(len(arr)):
    #     if arr[i] == 5:
    #         var5+=1
    #     elif arr[i] == 10:
    #         var5-=1
    #         var10+=1
    #     elif arr[i] == 15:
    #         if var10>0:
    #             var10-=1
    #         else:
    #             var5-=2
    #     if var5<0:
    #         break
    # if var5 >= 0:
    #     print('YES')
    # else:
    #     print('NO')
# l = [1,2,3,4,5]
# z= len(l)
# # print(z)
# i=0
# for i in range(70, 81):
#     print(i)
#     i+=1
# m1=[]
# m2=[]
# m3=[]
# a, b = list(map(int, input().split()))
#
# for _ in range(a):
#     l = list(map(int, input().split()))
#     m1.append(l)
# for _ in range(a):
#     l = list(map(int, input().split()))
#     m2.append(l)
# for _ in range(a):
#     l = [None]*b
#     m3.append(l)


# for i in m1:
# #     print(*i)
# for i in range(a):
#     for j in range(b):
#         m3[i][j] = m1[i][j]+m2[i][j]
# for i in m3:
#     print(*i)
# m= [[1,2,3],
#     [4,5,6],
#     ]
# n=[[3,2,1,0],
#    [1,2,3,4],
#    [4,3,2,1]]
# # o=[17 15 13 11]
# # [41 36 31 26]
#
# m1=[[0,0,0,0],
# [0,0,0,0]]
#
#
#
# for i in range(len(m)):
#     for j in range(len(n[0])):
#         for k in range(len(n)):
#             sum=0
#             m1[i][j] += m[i][k]*n[k][j]
# for i in m1:
#     print(*i)







            # print(m[i][j], m[j][i], end= ',')
    # print()
# print(m[j][i])























