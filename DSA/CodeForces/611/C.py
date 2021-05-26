# for _ in range(int(input())):
n = int(input())
l = list(map(int,input().split()))
s  =set(l)
l1 = [i for i in range(1,n+1) if i not in s]
m = len(l1)//2
l1 = l1[m+1:]+l1[:m]+[l1[m]]

for i in range(n-1,-1,-1):
    if l[i] == 0:
        l[i] = l1.pop()
#         while 1:
#             p = l1.pop(0)
#             if p!=i+1:
#                 l[i] = p
#                 break
#             else:
#                 l1.append(p)
# #


print(*l)