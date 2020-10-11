l = [None]*100
l[0] = input('enter root:')
n1 = int(input('enter no of connections:'))
for i in range(n1):
    a,b,c = input('enter 3').split()
    k = l.index(a)+1
    if c == 'l':
        l[2*k-1] = b
    else:
        l[2*k] = b

print(l)
for i in range(0,len(l),3):
    if l[2*i] == None and l[2*i-1] == None:
        print(l[i])



