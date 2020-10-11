# arr=[1,4,3,2]
# m1= arr[0]
# m2=arr[0]
# c1=0
# c2=0
# for i in range(len(arr)):
#     if arr[i]>m1:
#         m1 =arr[i]
#         c1+=1
#     if arr[i] < m2:
#         m2 = arr[i]
#         c2+=1
# # print(c1,c2)
# s=[]
# def push(s,data):
#     s.append(data)
# def pop(s):
#     s.pop()
#
# while 1:
#     print("1. push")
#     print("2.pop")
#     c = int(input("enter choice"))
#     if c == 1:
#         data = int(input("element"))
#         push(s,data)
#         print(s)
#     if c==2:
#         pop(s)
#         print(s)
# # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# n,k = list(map(int,input().split()))
# arr=list(map(int,input().split()))
# c=0
#
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if (arr[i]+arr[j])%k == 0:
#             c+=1
# print(c)
# //////////////////////////////////////////////////////////////
# n=int(input())
# arr = list(map(int,input().split()))
# d={}
# c=0
# c1=0
# for i in range(len(arr)):
# n = list(map(int,input().split()))
# l = []
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         l.append([n[i]-n[j]])
# print(l)
# x=[]
# for i in range(len(l)-1):
#     s=abs((l[i]-l[i+1]))
#
#     x.append(s)
#
# print(x)
# '''''''''''''''''''''''''''''''''''''''''

s='bbbaaaccc'
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


a=max(d.values())
l=[]
for i in d.keys():
    if d[i] == a:
        l.append(i)
print(min(l))
























