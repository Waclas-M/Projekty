file = open("dane1_3.txt",'r')
A = file.readlines()

największa_suma = 0
segemnt_dop = ""

for liczba in range(0,len(A)):

    print(liczba)

    for x in range(2,len(A)):

        segment = A[liczba:x]
        suma_segmentu = 0
        for i in segment:
            i = i.strip()
            i = int(i)
            suma_segmentu +=i


        if suma_segmentu > największa_suma:
            największa_suma = suma_segmentu
            segemnt_dop = segment



print(f"{segemnt_dop}\n::{największa_suma}")
