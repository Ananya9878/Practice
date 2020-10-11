
s=input()
t=input()
k=int(input())
b=min(len(s),len(t))
p=0
for i in range(b):
    if s[i] != t[i]:
        break
    p+=1
d = len(s)-p
a = len(t)-p
y = k-(d+a)
print(d,a,y)
if k >= len(t)+len(s):
    print('yes')

elif y%2==0 and y>=0:
    print('Yes')
else:
    print('No')





