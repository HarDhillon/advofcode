import pdb
#====================================================
list = []

for x in range(272091, 815433):
    list.append(x)

answers = []

#if any number in sequence is smaller than previous returns False
def checker_increasing(number):
    num0 = int(str(number)[:1])
    num1 = int(str(number)[1:2])
    num2 = int(str(number)[2:3])
    num3 = int(str(number)[3:4])
    num4 = int(str(number)[4:5])
    num5 = int(str(number)[5:])

    if num0 > num1:
        return False
    elif num1 > num2:
        return False
    elif num2 > num3:
        return False
    elif num3 > num4:
        return False
    elif num4 > num5:
        return False
    else:
        return True

#at least 1 pair or will return False
def checker_pairs(number):
    num0 = int(str(number)[:1])
    num1 = int(str(number)[1:2])
    num2 = int(str(number)[2:3])
    num3 = int(str(number)[3:4])
    num4 = int(str(number)[4:5])
    num5 = int(str(number)[5:])

    if num0 > num1:
        return True
    elif num1 == num2:
        return True
    elif num2 == num3:
        return True
    elif num3 == num4:
        return True
    elif num4 == num5:
        return True
    else:
        return False

def newrule(number):
    num0 = int(str(number)[:1])
    num1 = int(str(number)[1:2])
    num2 = int(str(number)[2:3])
    num3 = int(str(number)[3:4])
    num4 = int(str(number)[4:5])
    num5 = int(str(number)[5:])

    
#==========================================================


for number in list:
    #Debugging
    #pdb.set_trace()
    #Debugging

    length = str(number)
    if len(length) != 6:
        print (number, "is not 6 digits, skipping")
        continue

    if checker_increasing(number) == False:
        continue
    elif checker_pairs(number) == False:
        continue
    else:
        answers.append(number)

print (answers)
print ('Number of answers possible: ', len(answers))
