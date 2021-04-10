# l = [[1]]
#
# l = [[1, 2], [1,3], [1, 4]]
#
# l = [[1, 2, 5],[1, 3, 6], [1, 3, 7], [1, 3, 8], [1, 4] ]
#
# l = [[1,2,5], [1,3,6], [1,3,7,9], [1,3,8], [1,4]]

# 8
# 1 2
# 1 3
# 1 4
# 2 5
# 3 6
# 3 7
# 3 8
# 7 9

#{1:[2, 3, 4], 2: [5], 3:[6, 7, 8], 7:[9]}

l = []
d = {}

n = int(input('Enter No of coonections:'))
for _ in range(n):

    a, b = map(int, input().split())
    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]

root = int(input('Enter root: '))

l = [[root]]
temp_list = []

while 1:
    for i in l:
        #i= [1]
        current_node = i[-1]
        #[2, 3, 4]
        if current_node in d:
            connetion = d[current_node]
            for j in connetion:
                temp_list.append(i + [j])
        else:

            temp_list.append(i)

    if l == temp_list:
        break
    else:
        l = temp_list
        temp_list = []
    print(l)


#[1, 2, 3, 5, None, 6, 8, None, None, ]