s='@ack15'
special_characters = "!@#$%^&*()-+"
c1,c2,c3,c4 = 0,0,0,0
for i in range(len(s)):
    if (s[i].isdigit()):
        c1=1
    elif s[i].isupper():
        c2=1
    elif s[i].islower():
        c3=1
    elif s[i] in special_characters:
        c4=1
w = 4-(c1+c2+c3+c4)
n = 6-(len(s)+w)
n = max(0,n)
print(w+n)




