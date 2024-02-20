file = open('pi.txt','r')
file = file.readlines()
licznik = 0
ciog6 = []
for x in range(1,len(file)):
    czy_R = True
    czy_M = True
    ciog = file[x-1:x+5]

    for i in range(1,len(ciog)):

        if czy_R and ciog[i-1] >= ciog[i]:
            czy_R = False
        elif not czy_R and ciog[i-1] <= ciog[i]:
            czy_M = False
            break

    if czy_R == False and czy_M == True:
        licznik +=1
        ciog6.append(ciog)

print(licznik)






