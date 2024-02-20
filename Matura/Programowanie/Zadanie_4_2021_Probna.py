
#4.1
file = open("napisy.txt",'r')
file_r = file.read()
liczby = ['1','2','3','4','5','6',"7",'8','9','0']
wynik= 0
for liczba in liczby:
    ilosc=file_r.count(liczba)
    wynik = wynik+ilosc

print(wynik)

file.close()

#4.2

file = open("napisy.txt",'r')
file_r = file.readlines()

wiersz = 19
haslo = ""
for x in range(0,50):
    line = file_r[wiersz]
    line = line.strip()
    litera = line[x]
    haslo += litera
    wiersz += 20


print(haslo)
file.close()


#4.3
file = open("napisy.txt",'r')
file_r = file.readlines()
wyraz = ""
for line in file_r:
    line = line.strip()
    if line[1] == line[-1]:
        line += line[0]

    line_re = line[::-1]

    if line == line_re:
        litera = line[25]
        wyraz += litera

print(wyraz)
file.close()

#4.4
file = open("napisy.txt",'r')
file_r = file.readlines()
liczby=["1","2","3","4","5","6","7","8","9","0"]
zdanie = ""
licznik = 0
for line in file_r:
    line = line.strip()
    licz = ""
    liczby_lini = []
    for cyfra in line:
        if cyfra in liczby:
            licz +=cyfra
    if len(licz)==0 or len(licz)==1:
        continue
    if len(licz)%2==0:
        czesci = len(licz)/2
        czesci = int(czesci)
        for x in range(0,czesci*2,2):
            liczby_lini.append(licz[x:x+2])
    else:
        licz=licz[0:-2]
        czesci = len(licz) / 2
        czesci = int(czesci)
        for x in range(1,czesci):
            liczby_lini.append(licz[x-1:x])

    for x in liczby_lini:
        if int(x) < 65 or int(x) > 90:
            pass
        else:
            x = int(x)
            x = chr(x)
            if x == "X":
                licznik +=1
            zdanie += x
    if licznik == 3:
        break

print(zdanie)



