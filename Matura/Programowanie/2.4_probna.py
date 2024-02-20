file = open('krosno.txt','r')
file = file.readlines()
file_strip = []
for line in file:
    line = line.strip()
    file_strip.append(line)

n = 100

for k in range(1,n):
    for i in range(0,n-k):
        if int(file_strip[i]) < int(file_strip[i+k]):
            if i+k == n-1:
                print(k)
            pass
        else:
            break

