r = [1 ,3, 1, 3, 1, 4, 1,3 ,2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,7]
s ='zabc'
o=len(s)
l=[]
for i in range(len(s)):
    l.append(r[ord(s[i])-97])
e = max(l)


print(e*o)




