# def Bfs(d, start):
#     s = [start]
#     visited = set()
#     while len(s) > 0:
#         c = []
#         k = s.pop(0)
#         # print(k)
#         if k in visited:
#             continue
#         if k in d:
#             for i in d[k]:
#                 s.append(i)
#         visited.add(k)
#
#     return visited
#
#
# n, p = map(int, input().split())
# v = set()
# d = {}
# for i in range(p):
#     a, b = map(int, input().split())
#     if a in d:
#         d[a].append(b)
#     else:
#         d[a] = [b]
#     if b in d:
#         d[b].append(a)
#     else:
#         d[b] = [a]
#
# c=0
# for i in range(n):
#     if i not in v:
#         a = Bfs(d,i)
#         v=v.union(a)
#         c+=1
# print(c)
# Bfs(d,1)
# def merge(l1,l2):
#     if l1 is None:
#         return l2
#     p1 = l1
#     while p1.next is not None:
#         p1 = p1.next
#     p1.next = l2
#     return l1
# def quickSort(head):
# if head is None or head.next is None:
#         return head
#     left = None
#     right = None
#     lp,rp = left,right
#     p = head.next
#     while p is not None:
#         if p.data>=head.data:
#             if rp is None:
#                 right = Node(p.data)
#                 rp = right
#             else:
#                 rp.next = Node(p.data)
#                 rp = rp.next
#         else:
#             if lp is None:
#                 left = Node(p.data)
#                 lp = left
#             else:
#                 lp.next = Node(p.data)
#                 lp = lp.next
#         p = p.next
#     l = sort(left)
#     r = sort(right)
#     new_node = Node(head.data)
#     new_node.next = r
#     r = new_node
#     return merge(l,r)

# l1 = [1,2,4]
# l2 = [1,2,5]
# l3 = [1,3,6]
# l4 = [1,3,7]
# r1,r2,r3,r4 = 0,0,0,0
# for i in range(len(l1)):
#     r1^=l1[i]
#     r2^=l2[i]
#     r3^=l3[i]
#     r4^=l4[i]
# print(r1,r2,r3,r4)
# for _ in range(int(input())):
#     s = input()
#     c = 0
#     res = ''
#     t = s.split('0')
#     for i in range(len(t)):
#         if t[i] != '':
#             c+=1
#     print(c)

# s = 'AAAA'
# c=0
# for i in range(1,len(s)):
#     if s[i] == s[i-1]:
#         c+=1
# print(c)
#

# n = 13
# c = bin(13)[2:]
# a = ['1']*len(c)
# b = ['1']*len(c)
# for i in range(len(c)):
#     if c[i] == '1':
#         t = ''.join(a)
#         t1 = ''.join(b)
#         if int(t,2)>int(t1,2):
#             a[i] = '0'
#         else:
#             b[i] = '0'
# print(int(''.join(a),2)*int(''.join(b),2))

# n=6584651
# a,b=5,7
# l = list((str(n)))
# o,e = 0,0
# s=0
# for i in range(len(l)):
#     if i&1:
#         o+=int(l[i])*b
#     else:
#         e+=int(l[i])*a
# s=o+e
# while s>=9:
#     new_s = 0
#     m = list(str(s))
#     for i in m:
#         new_s+=int(i)
#     s = new_s
#
# print(s)



# for _ in range(int(input())):
#     s = int(input())
#     n = list(map(int,input().split()))
#     res = 0
#     for i in range(1,len(n)+1):

        # print(res)
        # print(i, n[i - 1])
        # if i>n[i-1]:
        #     print('First')
        #     break
        # else:
    #     a= i-n[i-1]
    #     res+=a
    # if res&1:
    #     print('First')
    #     break
    # else:
    #     print('Second')
    #     break

# for _ in range(int(input())):
#     n,m = map(int,input().split())
#     a = [0,1]
#     c = 0
#     while len(a)<10:
#         a.append(a[-1]+a[-2])
#     p = []
#     flag = True
#     while a:
#         if flag:
#             p.append(a.pop(0))
#             flag = False
#         else:
#             p.append(a.pop())
#             flag = True
#     print(p[:m])

# def dfs(mat,m,n,start,end):
#     s = [(start,0)]
#     visited = set()
#     while s:
#         p = s.pop(0)
#         if p[0] in visited:
#             continue
#         visited.add(p[0])
#         print(p)
#         x,y = p[0][0],p[0][1]
#         # if p[0] == end:
#         #     return True
#         conn = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
#         for i in conn:
#             a,b = i[0],i[1]
#             if a>=0 and a<m and b>=0 and b<n:
#                 if mat[a][b] == 0:
#                     k = (a,b)
#                     s.append((k,p[-1]+1))
#     return False
# mat = [[0,1,1,0],[0,0,0,0],[0,1,1,0]]
# m,n = len(mat),len(mat[0])
# start = (2,0)
# end = (0,0)
# print(dfs(mat,m,n,start,end))

import heapq
# def bfs(mat,m,n,start,end):
#     s = [[(mat[start[0]][start[1]],start)]]
#     heapq.heapify(s)
#     visited = set()
#     while s:
#         l = heapq.heappop(s)
#         p = l[-1]
#         if p[1] in visited:
#             continue
#         visited.add(p[1])
#
#         if p[1] == end:
#             return l
#         x,y = p[1][0],p[1][1]
#         conn = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
#         for i in conn:
#             a,b = i[0],i[1]
#             if a>=0 and a<m and b>=0 and b<n:
#                 if mat[a][b] != -1:
#                     heapq.heappush(s,l+[(p[0]+mat[a][b],(a,b))])
#     return False
#
# mat = [[4,-1,4,3,2],[2,-1,5,-1,3],[1,18,4,-1,2],[3,-1,3,25,0],[0,1,2,-1,4]]
# n,m = 5,5
# start = (0,0)
# end = (4,4)
# print(bfs(mat,m,m,start,end))
#
# s = 'ababa'
# if len(s) == 0:
#     print(True)
# if s == s[::-1]:
#     print(True)
# else:
#     d = {}
#     for i in range(len(s)):
#         if s[i] not in d:
#             d[s[i]] = [i]
#         else:
#             d[s[i]].append(i)
#

# a = (2**100)
# print(len(str(a)))
# for _ in range(int(input())):
#     a,b = map(int,input().split())
#     n = input()
#     l = []
#     for i in range(a):
#         l.append((int(n[:i]+n[i+1:]))%b)
#     print(max(l))

# l = [4,2,1,3]
# c=0
# for i in range(len(l)-1):
#     p = l[i:len(l)+1]
#     print(p)
#     m = min(p)
#     x = l.index(m)
#     l = l[:i]+l[i:x][::-1]
#     print(l)
# t = [[5,4],[6,4],[6,7],[2,3]]
# t = [[4,5],[6,7],[2,3]]
# t = [[5,4],[6,4],[6,7],[2,3]]
# t = [[4,5],[4,6],[6,7],[2,3],[1,1]]
# t = [[4,5],[4,6],[6,7],[2,3],[1,1],[1,1]]
# t = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
# # t = [[5,4],[6,4],[6,7],[2,3]]
# # t+=[[-1,-1]]
# t = [[1,1],[1,1],[1,1]]
# # t = [[1,1]]
# t = [tuple(i) for i in t]
# t = list(set(t))
# t.sort()
# dp = [[0]*(len(t)+1) for i in range(len(t)+1)]
#
# for i in range(len(t)+1):
#     for j in range(len(t)+1):
#         if i==0 and j==0:
#             dp[i][j] = 0
#         elif i==0 or j == 0:
#             dp[i][j] = 0
#         elif t[i-1][0]<t[j-1][0] and t[i-1][1]<t[j-1][1]:
#             a = dp[i-1][j-1] + 1
#             b = dp[i][j-1]
#             c = dp[i-1][j]
#             dp[i][j] = max(a, b, c)
#             # dp[i][j] = dp[i-1][j-1]+1
#         else:
#             dp[i][j] = max(dp[i][j-1], dp[i-1][j])
#             # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i-1][j-1])
# for i in dp:
#     print(i)
# print(dp[len(t)][len(t)])

# def minOperation(n,d={}):
#     if n <= 0:
#         return 0
#     if n in d:
#         return d[n]
#     if n & 1 == 0:
#         b = minOperation(n // 2, d)
#         # a = minOperation(n - 1, d)
#
#         d[n] = (b) + 1
#         return d[n]
#     else:
#         a = minOperation(n - 1, d)
#         d[n] = a + 1
#         return d[n]
    # # print(n)
    # if n <= 0:
    #     return 0
    # if n&1==0:
    #     a = minOperation(n-1)
    #     b = minOperation(n//2)
    #     return min(a,b)+1
    # else:
    #     a = minOperation(n-1)
    #     return a+1
# b = minOperation(10000)
# print(b)
# s = ["10","0001","111001","1","0"]
# # s = ["10","0","1"]
#
# m0,n1 = 1,1
# c = 0
# nc =0
# for i in range(len(s)):
#     a = s[i]
#     c0,c1 = a.count('0'),a.count('1')
#     print(c0,c1)
#     if c0<=m0 and c1<=n1:
#         c+=1
#     elif c0==m0 and c==n1:
#         nc+=1
# print(max(c,nc))

# a,b,c,d =1 ,1000000000 ,1 ,1000000000
# a,b,c,d =4,4,4,4
# c = 0
# mod = (10 ** 9) + 7
# x1 = (a ^ c) + (a ^ d)
# y1 = (b ^ c) + (b ^ d)
# print(x1,y1)
# c = x1 + y1
from operator import ixor
# a,b,c,d = 1,2,3,4
# l = [i for i in range(c,d+1)]
# c=0
# for i in range(a,b+1):
#     t = i^l[i]
#     c+=t
# print(c)
# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# c=0
# for i in range(n+1):
#     for j in range(i+1,n):
#         w = (a[i]*b[j]) - (a[j]*b[i])
#         print((a[i],b[i]),(a[j],b[i]))
#         c+=(w**2)
# print(c)
# print((1^3)+(1^4)+(2^3)+(2^4))
# b = [3,4,]
# print(ixor(1,b[0])+ixor(1,b[1])+ixor(2,b[0])+ixor(2,b[1]))
# print(1^(3+4+3+4))
# a,b,c,d = 1,2,3,4
# c=0
# for i in range(c,d+1):
#     c+=ixor()
# n,k = map(int,input().split())
# n,k = 3,1
# if k==1:
#     print(n**3)
# else:
#     while k>0:
#         a = n**3
#         k-=1
#         if k>=1:
#             h = str(a)
#             l = [int(h[i]) for i in range(len(h))]
#             s = sum(l)
#             n = s**3
#             k -= 1
#
#     print(n)
# sentence1 = "My name is Haley"
# sentence2 = "My Haley"
# a = sentence1.split()
# b = sentence2.split()
# print(a,b)
# g = [i.strip(b[i]) for i not in a]
#
# p = sentence1.strip(sentence2)
# print(g)
# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# nums = [42,11,1,97]
# nums = [13,10,35,24,76]
#
# c=0
# for i in range(len(nums)):
#     for j in range(1,len(nums)):
#         if i<j<len(nums):
#             if nums[i] + int(str(nums[j])[::-1]) == nums[j] + int(str(nums[i])[::-1]):
#                 c+=1
# print(c)
# s='ana'
# s = list(s)
# i = 0
# while s:
#     s.pop(i)
#     print(s)
#     i+=1
#
# print(s)
# l = ''.join(list(map(str,[1,1,0,1,1,1])))
# b = l.split('0')
# c=0
# for i in b:
#     if len(i)>c:
#         c=len(i)
# print(c)
# nums = [555,901,482,1771]
# l = list(map(str,nums))
# c=0
# for i in range(len(l)):
#     if len(l[i])&1==0:
#         c+=1
# print(c)

# s = "/u/love\i\\"
# # print(s.strip('/'))
# # s = s[::-1]
# t = []
# p = ''
# for i in range(1,len(s)-1):
#     if s[i].islower():
#         p+=s[i]
#     elif s[i] == '/' or s[i] == '\\':
#         t.append(p)
#         p = ''
# t.append(p[::-1])
# t = t[::-1]
# v = ''.join(t)
# print(v)
# n = 4
# s1='1101'
# s2='0011'
# s1 = list(s1)
# s2 = list(s2)
# res=0
# for i in range(n-1):
#     if s1[i] == s2[i]:
#         continue
#     else:
#         if s1[i+1] == s2[i+1]:
#             res+=1
#         else:
#             if s1[i]!=s1[i+1]:
#                 s1[i],s1[i+1] = s1[i+1],s1[i]
#                 res+=1
#             else:
#                 res+=1
# if s1[n-1] != s2[n-1]:
#     res+=1
# print(res)
# nums = [1,2,3,4,5]
# k=2
# res=0
# i = 0
# while len(nums)>1:
#
#     res += 1
#     if res == k:
#         print(nums[i])
#         nums.pop(i)
#         res=0
#
#     i = len(nums) % len(nums)
#     i+=1
#     print(i)
# print(nums)
































