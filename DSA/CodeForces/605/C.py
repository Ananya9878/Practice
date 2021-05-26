s,n = map(int,input().split())
st = input()
j = input().split()
res = 0
c = 0
for i in range(s):
    if st[i] in j:
        c+=1
    else:
        res+=((c*(c+1))//2)
        c = 0
res+=((c*(c+1))//2)
print(res)

