# K/k − król, H/h − hetman,
# W/w − wieża, G/g − goniec,
# S/s − skoczek, P/p − pionek.

Białe = ['K','W','S','H','G','P']
Czarne = ['k','w','s','h','g','p']


# .k......
# ........
# ........
# ....s...
# ....S...
# ........
# ........
# .......K

file = open('szachy.txt','r')
wszystkie_plansze = file.readlines()
rownowazne = 0
mixi = 1000
for rzad in range(1,len(wszystkie_plansze),9):
    plansza = wszystkie_plansze[rzad-1:rzad+7]
    wszyst_bierki = []
    for rzad_2 in plansza:
        rzad_2 =rzad_2.strip()
        for piony in rzad_2:
            if piony != '.':
                wszyst_bierki.append(piony)
    ile = len(wszyst_bierki)

    if ile%2 != 0:
        continue

    male = []
    duze = []
    for x in  wszyst_bierki:
        if x == x.upper():
            duze.append(x)
        elif x == x.lower():
            male.append(x.upper())
    male.sort()
    duze.sort()
    if male == duze:
        rownowazne +=1
        if ile < mixi:
            mixi = ile




print(rownowazne, mixi)