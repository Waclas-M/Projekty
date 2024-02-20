file = open('bin.txt','r')
file = file.readlines()
import math
for line in file:
    line = line.strip()
    wynik = ""
    a = line
    b = math.floor(int(line, 2) / 2)
    b = bin(b)
    b = b[2::]
    if len(a)>len(b):
        roznica = len(a)-len(b)
    b = "0"*roznica+b

    for i in range(1,len(a)+1):

        if a[i-1] == "1" and b[i-1] == "1":
            wynik = wynik+"0"
        elif a[i-1] == "0" and b[i-1] == "1":
            wynik = wynik + "1"
        elif a[i-1] == "1" and b[i-1] == "0":
            wynik = wynik + "1"
        elif a[i-1] == "0" and b[i-1] == "0":
            wynik = wynik + "0"

    print(wynik)

    if len(wynik)<8:
        wynik = wynik+"0"*(8-len(wynik))
    elif len(wynik)<16 and len(wynik)>8 :
        wynik = wynik+"0"*(16-len(wynik))
    elif len(wynik)<24 and len(wynik)>16:
        wynik = wynik + "0" * (24 - len(wynik))

