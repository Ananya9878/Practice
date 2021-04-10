n = 24
l=[]
for i in range(2,11):
    if n%i==0:
        l.append(i)
if len(l)==0:
    print(1)
else:
    print(max(l))