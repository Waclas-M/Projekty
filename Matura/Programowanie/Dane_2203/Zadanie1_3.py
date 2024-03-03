
# K/k − król, H/h − hetman,
# W/w − wieża, G/g − goniec,
# S/s − skoczek, P/p − pionek.




file = open('szachy_przyklad.txt','r')
wszystkie_plansze = file.readlines()
Białe_szach = 0
CZarne_szach = 0
for rzad in range(1,len(wszystkie_plansze),9):
    plansza = wszystkie_plansze[rzad-1:rzad+7]

    for miejsce in range(0,8):
        kolumna = ""
        for rzad_2 in range(0,8):
            print(plansza[rzad_2][miejsce])
            kolumna += plansza[rzad_2][miejsce]
        if 'W' in kolumna and 'k' in kolumna:
            index_W = kolumna.index('W')
            index_K = kolumna.index('k')
            nizszy= min(index_K,index_W)
            wyzszy = max(index_K,index_W)
            miejsce_W_k = kolumna[nizszy+1:wyzszy]

            ilosc_pust = len(miejsce_W_k)
            if ilosc_pust == miejsce_W_k.count('.'):
                Białe_szach +=1
            else:
                pass



        elif 'w' in kolumna and 'K' in kolumna:
            index_W = kolumna.index('w')
            index_K = kolumna.index('K')
            nizszy = min(index_K, index_W)
            wyzszy = max(index_K, index_W)
            miejsce_W_k = kolumna[nizszy+1: wyzszy]

            ilosc_pust = len(miejsce_W_k)
            if ilosc_pust == miejsce_W_k.count('.'):
                CZarne_szach += 1
            else:
                pass

    for x in plansza:
        if 'W' in x and 'k' in x:
            index_W = x.index('W')
            index_K = x.index('k')
            nizszy = min(index_K, index_W)
            wyzszy = max(index_K, index_W)
            miejsce_W_k = x[nizszy+1: wyzszy]
            ilosc_pust = len(miejsce_W_k)
            if ilosc_pust == miejsce_W_k.count('.'):
                Białe_szach += 1
            else:
                pass
        elif 'w' in x and 'K' in x:
            index_W = x.index('w')
            index_K = x.index('K')
            nizszy = min(index_K, index_W)
            wyzszy = (index_K, index_W)
            miejsce_W_k = x[nizszy+1: wyzszy]

            ilosc_pust = len(miejsce_W_k)
            if ilosc_pust == miejsce_W_k.count('.'):
                CZarne_szach += 1
            else:
                pass

print(CZarne_szach,Białe_szach)
