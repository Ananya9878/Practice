s='abc'
s1 = s[::-1]
# print(s1)
l=[]
l1=[]
for i in range(len(s)):
    l.append(ord(s[i]))
    l1.append(ord(s1[i]))
l2=[]
l3=[]
for i in range(len(l)):
    l2.append(abs(l[i] - l[i-1]))
    l3.append(abs(l1[i] - l1[i-1]))
print(l2)
print(l3)
if l2 == l3:
    print('Funny')
else:
    print('Not funny')
