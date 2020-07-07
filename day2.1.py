file = open('day2.info.txt')
fhandle = file.read().split(',')

sequence = list()
for indiv in fhandle:
    x=int(indiv)
    sequence.append(x)
#================================================
#above is fine

def opc1( a, b, c ):
    x = sequence[a] + sequence[b]
    sequence[c] = x

def opc2 (a, b, c ):
    x = sequence[a] * sequence[b]
    sequence[c] = x
#=============================================
#definitions

pos = 0

while True:
    if sequence[pos] == 99:
        print ("99 Found, Quitting Programm")
        print ('The new list is: ', sequence)
        quit()

    elif sequence[pos] == 1:
        opc1(sequence[pos+1], sequence[pos+2], sequence[pos+3])
        pos = pos + 4
        print ('opc1 triggered')
        print ('new pos=', pos)

    elif sequence[pos] == 2:
        opc2(sequence[pos+1], sequence[pos+2], sequence[pos+3])
        pos = pos + 4
        print ('opc2 triggered')
        print ('new pos=', pos)

    else:
        pos = pos + 1
        print('number is not 1, 2 or 9')
        print ('new pos=', pos)
