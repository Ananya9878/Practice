s='aab'
n=11
z = n//len(s)
count = s.count('a')
count*=z
a=s[:n%len(s)]
print(a)
count+=a.count('a')
print(count)




