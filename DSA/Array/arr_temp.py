l = ['2','3','5','7']
def prime(n):
    c=0
    t = str(n)
    for i in range(len(t)):
        if t[i] not in l:
            return False
    return True

n = 537

i=1
n=10
p = []
while len(p)<n:
    if prime(i):
        p.append(i)
    print(i,p)
    i+=1

