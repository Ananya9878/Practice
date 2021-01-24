# def fun(l,r):
#     if r < l:
#         return
#     if l & 1 == 0:
#         # print(l,'*')
#         fun(l+2,r)
#         print(l)
#
#     else:
#         fun(l+1,r)
# l,r = 5,30
# fun(l,r)

# def fun1(l,r):
#     if l > r:
#         return
#     if r & 1 == 0:
#         print(r)
#         fun1(l,r-2)
#     else:
#         fun1(l,r-1)
#
#
#
#
# l,r = 5,30
# fun1(l,r)

# def fun2(n):
#     if n == 0:
#         return
#     fun2(n-1)
#     print(n)
# n=30
# fun2(n)


# ........Count Even Number in Given Range
# def fun(l,r,i):
#     if l>r:
#         return i
#     if l & 1 == 0:
#         return fun(l+1,r,i+1)
#         # return k
#     else:
#         return fun(l+1,r,i)
#
#
# l,r,i = 5,30,0
# print(fun(l,r,i+1))

# ;;;;;Count even no in array

# def even(l,i,c):
#     if len(l) == i:
#         return c
#     # print(l[i],i)
#     if l[i] & 1 == 0:
#         return even(l,i+1,c+1)
#     else:
#         return even(l,i+1,c)
#
#
# l = [2, 3, 4, 5, 6, 7, 8]
# i=0
# c=0
# print(even(l,i,c))

# ;;;;;;;;;FIND minimum in array
# def mini(l,i,t):
#     if len(l) == i:
#         return t
#
#     if l[i] < t:
#         t = l[i]
#     return mini(l,i+1,t)
#
#
# l = [1,2,3,4,6,0]
# i=0
# t=100000
# print(mini(l,i,t))


# # ...............Find maximum in array
# def maxi(l,n,m):
#     if n == 0:
#         return m
#     if l[n-1]>m:
#         return maxi(l,n-1,l[n-1])
#     else:
#         return maxi(l,n-1,m)
#
# i,m = 0,-1
# l = [5,3,4,7,1,0]
# print(maxi(l,len(l),m))
# ..................MAX
# def maxi(l,n):
#     if n == 1:
#         return l[0]
#     t1 = l[n-1]
#     t2 = maxi(l,n-1)
#     return max(t1,t2)
    # if t1>t2:
    #     return t1
    # else:
    #     return t2
# .....................................




# ;;;;;Find sum of array
# def s(l,n,c):
#     if n == 0:
#         return c
#     return s(l,n-1,c+l[n-1])
#
# l = [1,2,3,4,5]
# print(s(l,len(l),0))

# find sum:
# def s(l,n):
#     if n == 0:
#         return l[0]
#     # t1 = l[n]
#     # t2 = s(l,n-1)
#     return (l[n]+s(l,n-1))
# print(s([1,2,3],2))

# def s1(n):
#     if n == 1:
#         return n
#     return (n+s1(n-1))
# print(s1(5))


# def s(l,n,c):
#     if n == 0:
#         return c
#     if l[n-1] & 1 == 0:
#         return s(l,n-1,c+l[n-1])
#     else:
#         return s(l,n-1,c)
#
#
# l = [1, 2, 3, 4, 5]
# print(s(l,len(l),0
# ......................Factorial
# def fact(n):
#     if n == 1:
#         return 1
#     return (n*fact(n-1))
#
# print(fact(5))
# # ..............MINIMUM
# def mini(l,n):
#     if n == 1:
#         return l[0]
#     return min(l[n-1],mini(l,n-1))
#
# l = [1,2,30,0]
# print(mini(l,4))

# '''''''Count k in lists
# def count_k(l,n,k):
#     if n == 0:
#         return 0
#     if l[n-1] == k:
#         return (1+count_k(l,n-1,k))
#     else:
#         return (count_k(l,n-1,k))
#
# l = [1,2,30,1,1,1,2,2,2]
# print(count_k(l,9,1))
# .......count eve numbers
# def count_k(l,n):
#     if n == 0:
#         return 0
#     if l[n-1] & 1 == 0:
#         return (1+count_k(l,n-1))
#     else:
#         return (count_k(l,n-1))
#
# l = [1,2,30,1,1,1,2,2,2]
# print(count_k(l,9))
# ;;;;;;;;;sum of even numbers
# def sum_even(l, n):
#     if n == 0:
#         return 0
#     if l[n-1] & 1 == 0:
#         return (l[n-1] + sum_even(l, n - 1))
#     else:
#         return (sum_even(l, n - 1))
#
# l = [1,2,30,1,1,1,2,2,2]
# print(sum_even(l,9))

# ;;;;;;;;;; return total even numbers
# def even(l,n,l1):
#     if n == 0 :
#         return l1
#     if l[n-1] & 1 == 0:
#         l1.append(l[n-1])
#     return even(l,n-1,l1)
#
# l = [1,2,3,4,5]
# print(even(l,5,l1=[]))

# def even1(l,n):
#     if n == 0:
#         return []
#     if l[n-1] & 1 == 0:
#         return [l[n-1]]+even1(l,n-1)
#     else:
#         return even1(l,n-1)
# l = [1,2,3,4,5]
# print(even1(l,5))
# ;;;;;;;;;;;;........
# def c(arr,l,r,n):
#     if n == 0:
#         return 0
#     if arr[n-1]>=l and arr[n-1] <= r:
#         return 1+c(arr,l,r,n-1)
#     else:
#         return c(arr,l,r,n-1)
#
# arr = [1,2,3,4,5,6,7,8]
# l,r = 3,6
# print(c(arr,l,r,len(arr)))
# .................

# def stk(arr,n):
#     if n == 0:
#         return []
#     # l1.append(arr[n-1])
#     return [arr[n-1]]+stk(arr,n-1)
#     # print(arr[n - 1])
#
# arr = [1,2,5,3,4,5]
# print(stk(arr,len(arr)))
# .....................Reverse Stack
# def insert1(arr,t):
#     if len(arr) == 0:
#         arr.append(t)
#         return arr
#     p = arr.pop()
#     arr = insert1(arr,t)
#     arr.append(p)
#     return arr
#
# def stk(arr):
#     if len(arr) == 0:
#         return 0
#     t=(arr.pop())
#     stk(arr)
#     insert1(arr,t)
#     return arr
#     # print(arr)
#
# arr = [1,2,5,3,4,5]
# print(stk(arr))




