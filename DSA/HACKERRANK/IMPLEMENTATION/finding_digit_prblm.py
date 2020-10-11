n=int(input())
# l=[]
# for i in range(n):
#     a=n%10
#     n=n//10
# l.append(a)
c=0
l= list(map(int,list(str(n))))
for i in range(len(l)):
    if l[i] !=0:
        if n%l[i]==0:
            c+=1
print(c)