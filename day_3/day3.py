print('Enter filename')
filename = input()

priority = 0
ascii_lower_deviation = 96 # used to simplify priority calcs
ascii_upper_deviation = 38
compartment_list = []
group_dict = {}

def remove_newline_from_string(cmprt_list):
    new_list = []
    for compartment in cmprt_list:
         new_list.append(compartment.strip('\n'))
       
    return new_list

def get_first_compartment(string):
    return string[:len(string)//2]

def get_second_compartment(string):
    return string[len(string)//2:]

def get_common_items(string1, string2):
    return ''.join(set(string1).intersection(string2))

def calc_priority(string):
    for letter in string:
        if letter.islower():
            return ord(letter) - ascii_lower_deviation
        else: 
            return ord(letter) - ascii_upper_deviation
        
def calc_priority_from_groups(cmprt_list):
    priority2 = 0
    while cmprt_list != []:
        group = [cmprt_list.pop() for _ in range(3)]
        priority2 += calc_priority(''.join(set(group[0]).intersection(group[1], group[2])))
    return priority2

with open(filename) as f:
    rucksack_items = f.readlines()

    for compartment in rucksack_items:
        compartment_list.append(compartment)
        priority += calc_priority(get_common_items(get_first_compartment(compartment),  get_second_compartment(compartment)))

    compartment_list = remove_newline_from_string(compartment_list)
    
    print('PART 1:\n' + str(priority))
    print('PART 2:\n' + str(calc_priority_from_groups(compartment_list)))
    