n=1
n1=100
l1=[]
for i in range(n,n1+1):
    x=i*i
    d = len(str(i))
    x = str(x)
    r = int(x[-d:])
    l = (x[:-d])
    if l == '':
        l = 0
    else:
        l = int(l)
    if r+l == i:
        l1.append(i)
if l1 == []:
    print('INVALID RANGE')
else:
    print(l1)


