i,j,k = list(map(int,input().split()))
l=[]
c=0
for q in range(i,j+1):
    # print(q,i,j)
    s = abs(q - (int(str(q)[::-1])))
    if s % k == 0:
        c+=1
print(c)



