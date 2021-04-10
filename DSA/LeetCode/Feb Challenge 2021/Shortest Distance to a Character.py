s = "loveleetcode"
c = "e"
l=[0]*len(s)
count = 100000
for i in range(len(s)):
    if s[i] == c:
        count = 0
    l[i] = count
    count+=1
count = 100000
for i in range(len(s)-1,-1,-1):
    if s[i] == c:
        count = 0

    l[i] = min(l[i],count)
    count+=1


print(l)



#
# l = [i for i in range(1,len(s)+1)]
# for i in range(len(s)):
#     if s[i] == c:
#         l[i] = 0
# print(l)
# for i in range(len(s)):
#     a,b = l[i],i
#     m = min(a,b)
#     l[i] = m
# print(l)
# for i in range(len(s)):
#     a,b = l[-i-1],i
#     m = min(a,b)
#     l[-i-1] = m
# print(l)
#
#
#
# print(l)
# # 1 2 3 4 5
# # 0 2 0 4 0
# # 0 1 0 3 0
# # 0 1 0 1 0

