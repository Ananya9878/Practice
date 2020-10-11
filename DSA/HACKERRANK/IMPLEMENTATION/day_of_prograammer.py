yr=int(input())
date=13
if 1700 < yr <= 1917:
    if yr%4 == 0:
        date = 12
if yr>1917:
    if (yr%400==0) or (yr%4 == 0 and yr%100 !=0):
        date = 12
if yr == 1918:
    date+=13
print(str(date)+'.09.'+str(yr))


