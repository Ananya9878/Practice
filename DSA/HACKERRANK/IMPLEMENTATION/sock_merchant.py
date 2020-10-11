from collections import Counter
n = int(input())
arr =  list(map(int,input().split()))
s = Counter(arr)
print(s)


c=0
for i in s.values():
    c+=i//2
print(c)


# print(l)
