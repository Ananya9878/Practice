s= 'DDUUDUDU'
c=0
c1=0
for i in range(len(s)):
    if s[i] == 'D':
        c+=1
    else:
        c-=1
    if c == 0:
        if s[i] == 'U':
            c1+=1
print(c1)

