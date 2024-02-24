file = open("dane2_3.txt",'r')
file_save = open("odp2_3.txt",'w')
file_read = file.readlines()

for line in file_read:
    gleb_lewo = 1
    gleb_prawo = 1
    line = line.strip()

    for i in range(1,len(line)):
        if line[i-1] == "[" and line[i] != "]" :
            gleb_lewo +=1
        if line[-i] == "]" and line[-i-1] != "[":
            gleb_prawo +=1

    if gleb_lewo > gleb_prawo:
        file_save.write(f"\n {gleb_lewo}")

    else:
        file_save.write(f"\n {gleb_prawo}")
