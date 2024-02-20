file = open("bin.txt",'r')
file = file.readlines()
ile = 0
max = 0
bin_max = ""
for line in file:
    line = line.strip()
    #2.2
    b = 0

    for i in range(1, len(line)):
        if line[i - 1] == line[i]:
            pass
        else:
            b += 1
        if i + 1 == len(line):
            b += 1

    if b <= 2:
        ile +=1
    else:
        pass
    #2.3
    if int(line,2) > max:
        max=int(line,2)
        bin_max = line



print(ile)
print(bin_max)