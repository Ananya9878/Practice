import bisect
n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l = [l1[i]-l2[i] for i in range(n)]
l.sort()
res = 0
c=0
s,e = 0,n-1
pairs = 0
for i in range(n - 1, -1, -1):
  if l[i] <= 0: break
  index = bisect.bisect_left(l, -1 * (l[i] - 1))
  pairs += i - index
print(pairs)


