n,h,x = map(int,input().split())
l = list(map(int,input().split()))
m = max(l)
if m+x>=h:
    print('YES')
else:
    print("NO")

