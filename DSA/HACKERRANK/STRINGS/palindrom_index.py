# s='aaab'
# s1 = list(s[::-1])
# a = list(s)
# if a == s1:
#     print(-1)
# else:
#     for i in range(len(s)):
#
#         if s[i]!=s1[i]:
#             print(a[i],s1[i])
#             x = s[i]
#             print(x)
#             s1.remove(x)
#             t = a.index(x)
#             a.remove(x)
#             break
#
#     if a == s1:
#         print(t)
#     else:
#         print(-1)
# **********************************************************************888
s='baa'
s1=s[::-1]
n=len(s)
flag = True
i=0
while i<len(s) and s != s[::-1]:
    a = s[:i]+s[i+1:]
    b = s1[:(n-i-1)]+s1[(n-i):]
    # print(a,b)
    if a == b:
        flag = False
        break
    i+=1
if flag:
    print(-1)
else:
    print(i)








