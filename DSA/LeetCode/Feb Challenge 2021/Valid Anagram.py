s = "aacc"
t = "ccac"
st = set()
if set(s)!=set(t):
    print(False)

d1={}
d2={}

for i in s:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1

for i in t:
    if i not in d2:
        d2[i]=1
    else:
        d2[i]+=1


if d1==d2:
    print(True)
else:
    print(False)

