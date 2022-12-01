print('Enter filename')
filename = input()

currentMaxCalory = 0
currentElf = 1

with open(filename) as f:
    caloryList = f.readlines()
    caloryCount = 0
    if len(caloryList) != 0:
        for calory in caloryList:
            if calory != '\n':
                caloryCount += int(calory)
            else: 
                caloryCount = 0
                currentElf += 1
            if caloryCount >= currentMaxCalory:
                currentMaxCalory = caloryCount
                currentMaxElf = currentElf

        print('Max calory is: ' + str(currentMaxCalory) + '\nCarried by elf: ' + str(currentMaxElf))
    else:
        print('No elves')