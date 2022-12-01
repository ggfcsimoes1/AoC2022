print('Enter filename')
filename = input()

total_calory_list = []
current_max_calory = 0
current_elf = 1

def getTop3FromList(list): # gets top 3 elements from list by popping the max 3 times
    i=3
    new_list = []
    for el in list:
        while i > 0:
            maxel = max(list)
            list.remove(maxel)
            new_list.append(maxel)
            i -= 1
    return new_list

with open(filename) as f:
    calory_list = f.readlines()
    calory_count = 0
    if len(calory_list) != 0:
        calory_list.append('\n')  # Hack, makes input parsing easier 
        for calory in calory_list:
            if calory != '\n':
                calory_count += int(calory)
            else: 
                total_calory_list.append(calory_count)
                calory_count = 0
                current_elf += 1
            if calory_count >= current_max_calory:
                current_max_calory = calory_count
                current_max_elf = current_elf

        print('Max calory is: ' + str(current_max_calory) + '\nCarried by elf: ' + str(current_max_elf))
        print('Max elves list: ' + str(getTop3FromList(total_calory_list)))
    else:
        print('No elves')


