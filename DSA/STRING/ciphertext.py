# s='Ananya'
# k=4
# s1='esesce'
# l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# l1=l[k:]+l[:k]
# # print(l1)
#
# s2=''
# for i in s:
#     if i.isupper():
#         s2+=l1[l.index(i.lower())].upper()
#     else:
#         q = l.index(i)
#         s2+=l1[q]
# print(s2)
# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# s='Anany a'
# s1='ererce'
# l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# l1=[ '@',';',"'",'$','3','%','&','-','8','+','(',')','?','!','9','0','1','4','#','5','7',':','2','"','6','*']
# s2=''
# for i in s:
#     if i == ' ':
#         s2+=i
#     elif i.isupper():
#         s2+=l1[l.index(i.lower())].upper()
#     else:
#         s2+=l1[l.index(i)]
# print(s2)
# # /////////////////////////////////////////// Decode/////////////////////////////////////////////////////////////#
# s='8 )9:3 697'
# s1='ererce'
# l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# l1=[ '@',';',"'",'$','3','%','&','-','8','+','(',')','?','!','9','0','1','4','#','5','7',':','2','"','6','*']
# s2=''
# for i in s:
#     if i == ' ':
#         s2+=i
#     elif i.isupper():
#         s2+=l[l1.index(i.lower())].upper()
#     else:
#         s2+=l[l1.index(i)]
# print(s2)
# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# s='Abcxyz'
# s1=''
# k=800
# for i in s:
#     if i.isupper():
#         i = i.lower()
#         q = (ord(i)-97+k)%26
#         s1+=chr(q+97).upper()
#     else:
#         q = (ord(i) - 97 + k) % 26
#         s1 += chr(q + 97)
#
#     print(q)
# print(s1)
# ///////////////////////////////////////////
s='O hbm gmapz ct am vsofh tcf hvs psgh dfh ct am zwts. Zwys hvwg mf sjfm gbuz mf ct if zmt...W kobbo giddcfh i hc oqvwsjwbu mcif rfsoa obr voddwbsgg hvoh i rsgsfjs. O dfcawgs xp hy fvibuo tizz vcbsghm y gohv fovibuo.'
s1=''
s = s.lower()
k=12
for i in s:
    if i == ' ':
        s1+=' '
    if i.isupper():
        i = i.lower()
        q = (ord(i)-65+k)%26
        s1+=chr(q+65).upper()
    elif i.islower():
        i = i.upper()
        q = (ord(i) - 65 + k) % 26
        s1 += chr(q + 65).lower()

    # print(q)
print(s1)


