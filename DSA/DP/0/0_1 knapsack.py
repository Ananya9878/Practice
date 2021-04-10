# def knap(p,w,c,i,d):
#
#     if i == 0:
#         return 0
#     if c == 0:
#         return 0
#     if (c,i) in d:
#         return d[(c,i)]
#     if c>=w[i-1]:
#         a = knap(p,w,c-w[i-1],i-1,d)+p[i-1]
#     else:
#         a = 0
#     b = knap(p,w,c,i-1,d)
#     d[(c,i)] = max(a,b)
#     print("function cll for", c, i,max(a,b))
#     return max(a,b)
#
# profit = [5,3,3,3,3]
# weight = [5,3,3,3,3]
# c = 8
# d = {}
# n = len(profit)
# g = knap(profit,weight,c,n,d)
# print(g)
#
#
#
def knap(p,w,c,i,d):
    if i == 0:
        return 0
    if c == 0:
        return 0
    if d[c][i] != -1:
        return d[c][i]
    if c>=w[i-1]:
        a = knap(p,w,c-w[i-1],i-1,d)+p[i-1]
    else:
        a = 0
    b = knap(p,w,c,i-1,d)
    d[c][i] = max(a,b)
    print("function cll for", c, i,max(a,b))
    return max(a,b)

profit = [5,3,3,3,3]
weight = [1,1,1,1,1]
c = 5
n = len(profit)
d = [[-1]*(n+1) for i in range(c+1)]
g = knap(profit,weight,c,n,d)
print(g)




