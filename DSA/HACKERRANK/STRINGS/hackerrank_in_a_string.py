s='hackerrank'
s1='hackerworldrankfgf'
flag = 1
j = 0
for i in range(len(s1)):
    if s1[i] == s[j]:
        j+=1
    if j == 10:
        print('yes')
        flag = 0
        break
if flag == 1:
    print('No')