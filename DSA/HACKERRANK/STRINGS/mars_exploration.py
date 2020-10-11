s='SOSOOSOSOSOSOSSOSOSOSOSOSOS'
s1='SOS'
x = len(s)
w = x//3
c=0
for i in range(0,x,3):
    s2 = s[i:i+3]
    for j in range(3):
        if s1[j] != s2[j]:
            c+=1
print(c)
