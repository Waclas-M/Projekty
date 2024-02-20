bin = []
def zamiana_dec_Bin(n):

    while n > 1:
        reszta = n%2
        n = n / 2
        if reszta >= 1:
            reszta = 1
        else:
            reszta = 0
        bin.append(reszta)

zamiana_dec_Bin(245)
bin.reverse()
b = 0

for i in range(1,len(bin)):
    if bin[i-1] == bin[i]:
        pass
    else:
        b +=1
    if i+1 == len(bin):
        b += 1

print(b)