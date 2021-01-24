l=[2,3,-6,4,6,-3]
l1=[]
for j in range(len(l)):
    s=0
    for i in range(j,len(l)):
        s+=l[i]
        l1.append(s)
# print(l1)

# kadane algo:
m=-11000
t=0
start,end = 0,0
for i in range(len(l)):
    t+=l[i]
    if t<0:
        t=0
        start = i+1
    if t>m:
        m = t
        end = i+1
#     print(t,m)
# print(m,start,end)
# print(l[start:end])

k=3
m=-11000
t=0
start,end = 0,0
for i in range(len(l)):
    # start movements
    if i - start>=k:
        t-=l[start]
        start+=1
        if t<0:
            start=i
            t=0
    t += l[i]
    # included or not
    if t<0:
        t=0
        start = i+1

    if t>m:
        m = t
        end = i+1
    print(t,m)
print(m,start,end)
print(l[start:end])
