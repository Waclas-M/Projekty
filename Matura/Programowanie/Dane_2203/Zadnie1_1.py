file = open('szachy.txt','r')
wszystkie_plansze = file.readlines()
maxi = 0
puste_plansze = 0

for rzad in range(1,len(wszystkie_plansze),9):
    plansza = wszystkie_plansze[rzad-1:rzad+7]
    ile = 0
    for miejsce in range(0,8):
        kolumna = ""
        puste = 0
        for rzad_2 in range(0,8):
            print(plansza[rzad_2][miejsce])
            kolumna += plansza[rzad_2][miejsce]

        if kolumna.count('.')== 8:
            puste+=1
            ile+=1
        print("________")
    if ile > maxi:
        maxi = ile
    if ile > 0:
        puste_plansze +=1


print( maxi,puste_plansze)