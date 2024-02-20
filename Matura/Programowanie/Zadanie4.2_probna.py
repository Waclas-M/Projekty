file = open('liczby.txt','r')
file = file.readlines()
# M a b
import math
i = 0

def potega(a,x,M):
    if x == 0:
        return 1
    if x % 2 == 0:
        y = potega(a,x//2,M)
        return (y*y)%M
    else:
        y = potega(a,(x-1)/2,M)
        return (y*y*a)/M

def czy_pierwsza(M):
    for x in range(2,M):
        if M % x == 0:
            return False
    return True

liczba_M_pierwszych = 0
liczba_wspolnych_dzielnikow = 0
trojki = 0

for line in file:
    line = line.strip()

    index = line.index(" ")

    M = line[0:index]
    line = line[index+1::]

    index = line.index(" ")
    a = line[0:index]
    line = line[index+1::]

    b = line
    M = int(M)
    a= int(a)
    b = int(b)

    if czy_pierwsza(M) == True:
        liczba_M_pierwszych +=1

    if math.gcd(M,a) == 1:
        liczba_wspolnych_dzielnikow +=1

    for x in range(0,M):
        if potega(a,x,M) == b :
            trojki +=1
            break




print(liczba_M_pierwszych)
print(liczba_wspolnych_dzielnikow)
print(trojki)



