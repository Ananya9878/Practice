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


