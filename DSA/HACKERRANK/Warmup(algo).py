# mimi max..............
# arr = list(map(int, input().split()))
# x = sum(arr)
# # print(x)
# print(x-max(arr),x-min(arr))

# ///////////////////////////////////////////////
#
# n=int(input())
# arr = list(map(int, input().split()))
# for i in range(len(arr)):
#     if arr[i]<35:
#         print(arr[i])
#     elif arr[i]>35:
#         m = arr[i]%5
#         if m>=3:
#             print(arr[i]+5-m)
#         else:
#             print(arr[i])..........................

#         s = (arr[i]+5)

#         r = s%5
#         z=s-r
#         a=z-arr[i]
#         if a<3:
#             arr[i]=z
#             print(z)
#         else:
#             print(arr[i])
# ...............................................................................
# # ..............................................................................
# s,t = list(map(int,input().split()))
# a,b = list(map(int,input().split()))
# m,n = list(map(int,input().split()))
# s1 = list(map(int,input().split()))
# s2 = list(map(int,input().split()))
# l1=[]
# l2=[]
# for i in range(len(s1)):
#     l1.append(s1[i]+a)
# for i in range(len(s2)):
#     l2.append(s2[i]+b)
## c1=0
# c2=0
# for i in range(len(l1)):
#     if l1[i]>=s and l1[i]<=t:
#         c1+=1
# print(c1)
# for i in range(len(l2)):
#     if l2[i]>=s and l2[i]<=t:
#         c2+=1
# print(c2)
# ..................................................................................:
# #     .........................................................................................
# x1,v1,x2,v2 = list(map(int, input().split()))
# if x1>x2 and v2>v1 or x2>x1 and v1>v2:
#     print('Yes')
# else:
#     print('No')
# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# # ...............................................................................................
# a = [2,4]
# b=[16,32,96]
# m=min(b)
# f=[]
# import math
# def lcm(a):
#     lcm = a[0]
#     for i in range(1,len(a)):
#         lcm = lcm*a[i]//math.gcd(lcm,a[i])
#     return lcm
# f.append(lcm(a))
# print(f)
# i=1
# while i<=len(f):
#     for j in range(len(a)):
#         k = f[i-1]*a[j]
#         if k not in f:
#             if k<=m:
#                 f.append(k)
#             else:
#                 break
#     print(f[i-1], f)
#     i+=1
# c=0
#
# for j in range(len(f)):
#     flag=True
#     k=f[j]
#     for i in range(len(b)):
#         if b[i]%k!=0:
#             flag = False
#     if flag:
#         c+=1
# # print(c)
# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# s=
# for i in range(len(s)):
#     if s[i] == '(':
#         s1+=1
#     else:
#         s1-=1
#     if s1 < 0:
#         break
#
#
# if s1 == 0:
#     print('BALANCED')
# else:
# #    prin]t('UNBALANCED')
# s = '[({})]'
# b1=0
# b2=0
# b3=0
# v = len(s)//2
#
# l=[]
# c=len(l)//2
# for i in range(len(s)):
#     if s[i] == '[':
#         l.append(s[i])
#         b1+=1
#     elif s[i] == '(':
#         l.append(s[i])
#         b2+=1
#     elif s[i] == '{':
#         l.append(s[i])
#         b3+=1
# for i in range(len(s)):
#     if s[v] == ']':
#         l.append(s[i])
#         b1+=1
#     elif s[v] == ')':
#         l.append(s[i])
#         b2+=1
#     elif s[v] == '}':
#         l.append(s[i])
#         b3+=1
#
# if s[v] == l[v]:
#     print('Yes')
# else:
#     print('No')




# # print(b1,b2,b3)
# n = int(input())
# arr = list(map(int,input().split()))
# m = max(arr)
# m1 = min(arr)
# c1=0
# c2=0
# print(m,m1)
# for i in range(len(arr)):
#     if arr[i]>m:
#         c1+=1
#     elif arr[i]<m:
#         c2+=1
#     elif arr[i]>m1:
#         c1+=1
#     elif arr[i]<m1:
#         c2+=1
# print(c1,c2)

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# s='{[()]}'
# c1=0
# c2=0
# c3=0
# c4=0
# c5=0
# c6=0
# temp=''
# for i in range(len(s)):
#     if s[i] == "(":
#         c1+=1
#         temp=s[i]
#     if s[i] == ")":
#         if temp == "(":
#             c2+=1
#             temp = s[i-2]
#         else:
#             break
#     if c2>c1:
#         break
#
#     if s[i] == "[":
#         c3+=1
#         temp=s[i]
#
#     if s[i] == "]":
#         if temp == "[":
#             c4+=1
#             temp = s[i-2]
#         else:
#             break
#     if c4>c3:
#         break
#
#
#     if s[i] == "{":
#         c5+=1
#         temp=s[i]
#
#     if s[i] == "}":
#         if temp == "{":
#             c6+=1
#             temp = s[i-2]
#         else:
#             break
#     if c6>c5:
#         break
#
# if c1 == c2 and c3==c4 and c5 == c6:
#     print('YES')
# else:
#     print('NO')
s='[]'
st=[]
flag = True
for i in range(len(s)):
    if s[i] == '(':
        st.append(s[i])
    if s[i] == ")":
        if len(st)>0:
            if st[-1] == '(':
                st.pop()
            else:
                flag = False
        else:
            flag = False


    if s[i] == '{':
        st.append(s[i])
    if s[i] == "}":
        if len(st)>0:
            if st[-1] == '{':
                st.pop()
            else:
                flag = False
        else:
            flag = False


    if s[i] == '[':
        st.append(s[i])
    if s[i] == "]":
        if len(st)>0:
            if st[-1] == '[':
                st.pop()
            else:
                flag = False
        else:
            flag = False

if len(st) != 0:
    flag = False
if flag:
    print("yes")
else:
    print('no')



































