s='qmExzBIJmdELxyOFWv LOCmefk TwPhargKSPEqSxzveiun'
# s = set(s)
d={}
for i in range(len(s)):
    k = s[i]
    if k.isupper():
        k = k.lower()
    if k not in d:
        d[k] = 1
    else:
        d[k]+=1
c= len(d)-1
if c == 26:
    print('panagram')
else:
    print('not')