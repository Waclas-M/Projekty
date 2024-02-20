file = open("konta.txt",'r')
file = file.readlines()

Konta = []
#zadanie 4.1
for line in file:
    line = line.strip()
    koniec = line.index(" ")
    Pseudonim_A = line[0:koniec]
    Pseudonim_B = line[koniec+1::]
    if Pseudonim_A in Konta and Pseudonim_B in Konta:
        continue
    elif Pseudonim_A in Konta and Pseudonim_B not in Konta:
        Konta.append(Pseudonim_B)
    elif Pseudonim_A not in Konta and Pseudonim_B in Konta:
        Konta.append(Pseudonim_A)
    else:
        Konta.append(Pseudonim_A)
        Konta.append(Pseudonim_B)


print("Liczba kont:",len(Konta))
obserwowani = []
obserwatorzy = []
falszywe_konta = 0
falszywe_konta_pseud = []
obserwacje_wzajemne = 0
obserwcje = []
wzajemne = []
maxi = 0
prawdziwi_obserwatorzy = {}
obserwaje_licz = {}
for user in Konta:
    obserwujocy = 0
    obserwowani.clear()
    obserwatorzy = []
    for line in file:
        line = line.strip()
        if user in line:
            pass
        else:
            continue
        koniec = line.index(" ")
        Pseudonim_A = line[0:koniec]
        Pseudonim_B = line[koniec + 1::]

        if Pseudonim_B == user:
            obserwatorzy.append(Pseudonim_A)
            obserwujocy += 1
        elif Pseudonim_A == user:
            obserwowani.append(Pseudonim_B)
        else:
            pass

    if obserwujocy == 0:
        falszywe_konta += 1
        falszywe_konta_pseud.append(user)
    else:
        pass

    obserwaje_licz[user] = obserwatorzy

    for i in obserwowani:
        zaleznos = f"{user} {i}"
        zaleznos2 = f"{i} {user}"
        if user == "ZwierzakowySwiat" and i == "nie_taki_wolny_zolw":
            pass
        if i in obserwatorzy and zaleznos not in obserwcje and zaleznos2 not in obserwcje :
            obserwacje_wzajemne +=1
            obserwcje.append(f"{user} {i}")
            obserwcje.append(f"{i} {user}")

        else:
            pass

    if len(obserwowani) > maxi:
        maxi = len(obserwowani)
        imie = user
    else:
        pass

for user in Konta:
    prawdziwi_obserwatorzy_licz = len(obserwaje_licz[user])
    for x in obserwaje_licz[user]:
        if x in falszywe_konta_pseud:
            prawdziwi_obserwatorzy_licz -=1
        else:
            pass
    prawdziwi_obserwatorzy[prawdziwi_obserwatorzy_licz]=user

print("Fałszywych kont jest:",falszywe_konta,"\nsą to konta:" )
for i in falszywe_konta_pseud:
    print(i)
print("\nObserwuje siebie nawzajem:",obserwacje_wzajemne,"kont")
print("najwięcej obserwuje kont:",imie)
print("Najwięcej obsrwujących ma konto: ",prawdziwi_obserwatorzy[max(prawdziwi_obserwatorzy.keys())])









