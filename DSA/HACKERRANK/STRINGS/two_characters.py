s='asdcbsdcagfsdbgdfanfghbsfdab'
l= list(set(list(s)))
l1=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        l1.append((l[i],l[j]))
l2=[]
for p in l1:
    new_s = ''
    flag = True
    for i in s:
        if p[0] == i or p[1] == i:
            if new_s == '':
                new_s+=i
            elif new_s[-1] != i:
                new_s+=i
            else:
                flag = False
                break
    if flag:
        l2.append(len(new_s))
if len(l2) == 0:
    print(0)
else:
    print(max(l2))





