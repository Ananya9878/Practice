l=[1,2,3,4]
# one pair
for i in range(len(l)):
    print(l[i])
#  2 pair
for i in range(len(l)):
    for j in range(i+1,len(l)):
        print((l[i],l[j]))


