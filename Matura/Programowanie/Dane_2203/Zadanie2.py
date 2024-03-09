Tablica_A = []
Plansza_B = []
s = 500
for b in range(s+1):
    Plansza_B.append(b)
for a in range(0,105,5):
    Tablica_A.append(a)

n = len(Tablica_A)

def tura(k):
    for i in range(s,0 ,-1):
        if 'x' == Plansza_B[i-Tablica_A[k]] and Plansza_B[i] != 'x':
            Plansza_B[i] = 'x'

Plansza_B[0] = 'x'
for k in range(len(Tablica_A)):
    tura(k)

if Plansza_B[s] == 'x':
    print("Sukces")

    print(Plansza_B.count('x'))