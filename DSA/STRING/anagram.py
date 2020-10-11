# s='listen'
# s1='silent'

# d1 = Counter(s)
# d2 = Counter(s1)
# print(d1)
# # print(d2)
# d1={}
# d2={}
# for i in s:
#     if i in d1:
#         d1[i] = d1[i]+1
#     else:
#         d1[i] = 1
#
# for i in s1:
#     if i in d2:
#         d2[i] = d2[i]+1
#     else:
#         d2[i] = 1
#
# if d1 == d2:
#     print('Anagram')
# else:
#     print('Not')
# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# s1='ram'
# s2='rammm'

# v1=set(s1)
# v2=set(s2)
# if v1 == v2:
#     print('yes')
# else:
#     print('no')
# /////////////////////////////////////////////////////////////////////////////////////
# s='rame'
# s2='raam'
# d1={}
# d2={}
# flag=True
# k=1
# for i in s:
#     if i in d1:
#         d1[i] = d1[i]+1
#     else:
#         d1[i] = 1
# for i in s2:
#     if i in d2:
#         d2[i] = d2[i]+1
#     else:
#         d2[i] = 1
# if set(s) == set(s2):
#     for i in d1.keys():
#         if abs(d1[i] - d2[i]) > k:
#             flag = False
#             break
# else:
#     flag = False
# if flag:
#     print('yes')
# else:
#     print('no')
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
s='ramaaaa'
s2='raame'
x,y = 1,2
d1={}
d2={}
cost=0
for i in s:
    if i in d1:
        d1[i] = d1[i]+1
    else:
        d1[i] = 1
for i in s2:
    if i in d2:
        d2[i] = d2[i]+1
    else:
        d2[i] = 1
for i in d2.keys():
    if i in d1:
        d=max(0, (d2[i] - d1[i]))
        cost+=d*x
    else:
        cost+=d2[i]*y
print(cost)




