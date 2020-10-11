s='baab'
s1 = list(s)
i=1
while i<len(s1):
    if s1[i] == s1[i-1]:
        s1.pop(i)
        s1.pop(i-1)
        if i>1:
            i-=1
    else:
        i+=1
a = ''.join(s1)
if len(a) == 0:
        print('Empty String')
else:
    print(a)



