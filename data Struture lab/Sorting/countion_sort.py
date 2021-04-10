arr = [3,6,1,8]
a = [0]*(max(arr)+1)
for i in arr:
    a[i] = 1
print(a)
l=[]
for i in range(len(a)):
    if a[i] == 1:
        l.append(i)
print(l)
