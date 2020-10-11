n = 'vsmm hcobyi gcc gcc aiqv w kog o ywbro ot dfgb xc pzyz obds ood a fvho vc hiabs gc qv a pvh v xoro odbodb tssz yfomo obr bck w bjf sjsf kobb ' \
    'zcgs i wb obm qogs dfcawgs as i kwzz ps awbs ozkmg w zcjs i obobmo'
k=12
s1=''
for i in range(len(n)):
    if i == 80:
        s1+='\n'
    if n[i] == ' ':
        s1+=' '
    else:
        s = (ord(n[i])-97+k)%26
        # print(s,chr(s+97))
        s1+=(chr(s+97))
print(s1)