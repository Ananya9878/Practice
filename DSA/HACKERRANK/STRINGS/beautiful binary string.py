s='0100101010'
c=0
s = list(s)
for i in range(0,len(s)):
    if s[i:i+3]== list('010'):
        if s[i+2] == 0:
            s[i+2] =1
        else:
            s[i+2] = 0
        c+=1

print(c)
