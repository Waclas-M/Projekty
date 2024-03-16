plik = open('galerie.txt','r')
plik_read = plik.readlines()

Kraje = []
Miasta = []

for line in plik_read:
    line = line.strip()
    przerwa = line.index(" ")
    kod_kraju = line[0:przerwa]
    line = line[przerwa+1::]
    przerwa = line.index(" ")
    miasto = line[0:przerwa]

    Kraje.append(kod_kraju)
    Miasta.append(miasto)

Kraje.sort()
liga = set(Kraje)
for x in liga:
   print(x,Kraje.count(x))




