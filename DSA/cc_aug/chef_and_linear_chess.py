N,K =4,7
l=[4,3,2,8]
l1=[]
for i in range(N):
    if K%l[i] == 0:
        l1.append(((K//l[i])-1,l[i]))
if l1==[]:
    print(-1)
else:
    s=(min(l1))
    print(s[1])

