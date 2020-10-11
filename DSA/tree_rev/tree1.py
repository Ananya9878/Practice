n = int(input('Enter no of nodes'))
d = {}

for i in range(n-1):
    a, b = map(int,input().split())
    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]
    print(d)

root = int(input("Enter root"))

tree = [[root]]

while 1:
    temp = []
    for i in tree:
        current_node = i[-1]
        if current_node in d:
            connected_node = d[current_node]
            for j in connected_node:
                temp.append(i+[j])
        else:
            temp.append(i)
    if temp == tree:
        break
    tree = temp
print(tree)
