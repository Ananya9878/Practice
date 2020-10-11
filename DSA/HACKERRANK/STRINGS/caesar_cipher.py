s='abcdefghijklmnopqrstuvwxyz'
k=2
k = k%26
s1='middle-Outz!'
l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l=l1[k:]+l1[:k]
print(l)
s2=''
for i in s1:
    for i in s1:

        if i.isupper():
            s2 += l[l1.index(i.lower())].upper()
        elif i.islower():
            q = l1.index(i)
            s2 += l[q]
        else:
            s2+=i

print(s2)