


n=int(input())
s=''
stack=[s]

for i in range(n):
    l=input().split()
    if l[0] == '1':
        s = stack[-1]
        s+=l[1]
        stack.append(s)
    elif l[0] == '2':
        s = stack[-1]
        s = s[:-int(l[1])]
        stack.append(s)
    elif l[0] == '3':
        print(stack[-1][int(l[1])-1])
    else:
        stack.pop()






















