fname = open('day1.info.txt')
fhandle = fname.read().split()


sum = 0

for line in fhandle:
    number = int(line)
    fuel = int(number/3)-2
    xtrafuel = fuel
    while xtrafuel > 0:
        xtrafuel = int(xtrafuel/3) - 2
        if xtrafuel < 0:
             break
        sum +=  xtrafuel
    sum += fuel

print (sum)
