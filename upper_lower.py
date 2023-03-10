ifade = "merhaba benim adım amine"
new_ifade = ""

##1. Çözüm
for i in range(len(ifade)):
    if i % 2 == 0:
        new_ifade += ifade[i].upper()
    else:
        new_ifade += ifade[i].lower()
print(ifade)
print(new_ifade)

##2.Çözüm
for index, harf in enumerate(ifade):
    if index %2 == 0:
        new_ifade += ifade[index].upper()
    else:
        new_ifade += ifade[index].lower()

print(ifade)
print(new_ifade)
