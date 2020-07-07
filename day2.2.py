file = open('day2.info.txt')
fhandle = file.read().split(',')


input_arr = list()
for indiv in fhandle:
    x=int(indiv)
    input_arr.append(x)

def process_array(input_arr):
    arr = input_arr[:]

    for index in range(0, len(arr), 4):
        operator = arr[index]
        numberA = arr[arr[index + 1]]
        numberB = arr[arr[index + 2]]
        if operator == 99:
            return arr[0]
        elif operator == 1:
            arr[arr[index + 3]] = numberA + numberB
        elif operator == 2:
            arr[arr[index + 3]] = numberA * numberB

    return arr[0]

for noun in range(100):
    for verb in range(100):
        input_arr[1] = noun
        input_arr[2] = verb

        output = process_array(input_arr)

        if output == 19690720:
            print('Solution found, Noun = ',noun)
            print('Verb = ', verb)
            print('Solution is: ', 100 * noun + verb)
