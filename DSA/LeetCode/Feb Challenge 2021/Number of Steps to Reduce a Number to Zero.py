n=8
c=0
while n>0:
    if n&1==0:
        n = n//2
        c+=1
    else:
        n = n-1
        c+=1

print(c)
