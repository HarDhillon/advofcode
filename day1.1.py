fname = open('day1.info.txt')
fhandle = fname.read().split()


sum = 0
for line in fhandle:
    number = int(line)
    fuel = int(number/3)-2
    sum += fuel
    print (sum)
print (sum)
