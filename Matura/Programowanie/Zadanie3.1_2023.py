file= open("pi.txt",'r')

file = file.readlines()

pary_większe_90 = 0
# zadanie 3.1
for i in range(1,len(file)):
    a = file[i-1]
    b = file[i]

    a = a.strip()
    b = b.strip()

    liczba = a+b
    liczba = int(liczba)

    if liczba > 90:
        pary_większe_90 +=1
    else:
        pass

print(pary_większe_90)
