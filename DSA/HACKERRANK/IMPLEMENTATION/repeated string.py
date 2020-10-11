from collections import Counter
n = int(input())
arr = list(map(int,input().split()))
d = Counter(arr).values()
print(d)
delete=len(arr) - max(d)
print(delete)
