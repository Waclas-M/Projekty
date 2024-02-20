file = open("pi.txt",'r')
file_read_l = file.read()
file2 = open("pi.txt",'r')
file_read = file2.readlines()


dic = {}
line = []
# zadanie 3.2
for i in range(1,len(file_read)):
    wystopienia = 0
    a = file_read[i-1]
    b = file_read[i]

    wystopienia = file_read_l.count(a+b)

    a = a.strip()
    b = b.strip()

    liczba = a+b

    if liczba in dic.values():
        continue

    if wystopienia in dic.keys():
        if int(liczba) < int(dic[wystopienia]) :
            dic[wystopienia] = liczba
        else:
            continue

    dic[wystopienia] = liczba
    print(dic)


print("najmniejsza",dic[min(dic)],"\nNajwiększa",dic[max(dic)])

