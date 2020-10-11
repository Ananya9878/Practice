n,m,k = map(int,input().split())
s1= list(map(int,input().split()))
s2= list(map(int,input().split()))
s3= list(map(int,input().split()))

a = sum(s1)
b= sum(s2)
c = sum(s3)
while 1:
    print(a,b,c)
    if a == b and b == c:
        print(a)
        break
    elif a>b and a>c:
        k = s1.pop()
        a = a-k
    elif b > a and b > c:
        k = s2.pop()
        b = b - k
    elif c > b and c > a:
        k = s3.pop()
        c = c - k








