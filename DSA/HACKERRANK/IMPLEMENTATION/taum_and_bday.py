t = int(input())
for i in range(t):
    b,w = map(int,input().split())
    bc,wc,z = map(int,input().split())
    if bc>wc+z:
        a = b + w
        cost = a*wc+b*z
    elif wc > bc+z:
        a = b+w
        cost = a*bc +w*z
    else:
        cost = b*bc + w*wc
print(cost)

