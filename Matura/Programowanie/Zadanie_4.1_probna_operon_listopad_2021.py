


liczby_wesole = []
pamietnik = {}
def wesloa(liczba):
    wynik = 0

    liczba = str(liczba)


    if len(liczba) > 1:
        for x in liczba:
            x = int(x)
            wynik = wynik + x**2
        if wynik in skladniki:
            return 0,False,0
        else:
            skladniki.append(wynik)


    elif len(liczba) == 1:
        wynik = int(liczba)**2
        if wynik in skladniki:
            return 0, False,0
        else:
            skladniki.append(wynik)


    if wynik == 1:

        return skladniki,True
    elif wynik !=1:

        return wesloa(wynik)

for x in range(1,1000):
    if x in liczby_wesole:
        continue
    skladniki = []

    odp = None
    odp = wesloa(x)
    stan = odp[1]
    lista = odp[0]
    dlugosc = len(skladniki) + 1
    if stan == True:
        liczby_wesole.append(x)
        for i in skladniki:
            if i in liczby_wesole:
                pass
            else:
                liczby_wesole.append(i)

        pamietnik[x] = dlugosc
    else:
        continue

mxin = max(pamietnik.values())
print(mxin)
for x in pamietnik.keys():
    if pamietnik[x] == mxin:
        print(x)

print("\n\n\n_________________________________\n")

