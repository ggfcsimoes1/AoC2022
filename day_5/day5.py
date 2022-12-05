print('Enter filename')
filename = input()

def calculate_spaces(file):
    new_list = []
    i=0
    for line in file:
        if line == '':
            size_list = file[i-1]
        i += 1
    
    size_list = size_list.split(' ')

    while('' in size_list):
        size_list.remove('')

    for item in size_list:
        new_list.append(4 * int(item) - 1)

    return [new_list, size_list]

def parse_line(line, spaces_list):
    new_str = ''
    new_list = []
    new_list2 = []
    for i in range(len(line)+1): 
        if (i in spaces_list):
            i += 1
            new_list.append(new_str)
            new_str = ''
        else:
            new_str += line[i]
    for el in new_list:
        new_list2.append(el.strip()) 
    return new_list2
        
def parse_lines(lines, spaces_list):
    parsed_list = []
    for line in lines:
        if line != '':
            parsed_list.append(parse_line(line, spaces_list))
        else:
            return parsed_list[:-1]

def parse_moves(file):
    new_list = []
    startParse = False
    for line in file:
        if startParse:
            new_list.append([int(line.split(' ')[1]), int(line.split(' ')[3]), int(line.split(' ')[5])])
        if line == '':
            startParse = True
    return new_list

def populate_stacks(stack_list, spaces_list):
    new_stack_list = []
    for i in range(0,len(spaces_list)):
        stack_i = []
        for row in stack_list:
            if len(row[i]) != 0:
                stack_i.append(row[i][1])
        new_stack_list.append(stack_i)
    return new_stack_list

def make_moves(populated_stacks, parsed_moves):
    for moves in parsed_moves:
        move_amt = moves[0]
        move_from = moves[1]-1
        move_to = moves[2]-1
        for i in range(0, move_amt):
            removed_item = populated_stacks[move_from].pop(0)
            populated_stacks[move_to].insert(0, removed_item)
    return populated_stacks

def make_moves2(populated_stacks, parsed_moves):
    for moves in parsed_moves:
        move_amt = moves[0]
        move_from = moves[1]-1
        move_to = moves[2]-1
        
        if move_amt == 1:
                removed_item = populated_stacks[move_from].pop(0)
                populated_stacks[move_to].insert(0, removed_item)
        else:
            removed_items = []
            for i in range(0, move_amt):
                removed_item = populated_stacks[move_from].pop(0)
                removed_items.append(removed_item)
            for item in reversed(removed_items):
                populated_stacks[move_to].insert(0, item)
                
    return populated_stacks

def print_message(final_stacks):
    message = ''
    for item in final_stacks:
        message += item[0]
    return message

with open(filename) as f:

    file = f.read().splitlines()

    spaces_list = calculate_spaces(file)[0]
    stacks_list = calculate_spaces(file)[1]

    parsed_list = parse_lines(file, spaces_list)

    populated_stacks = populate_stacks(parsed_list, stacks_list)

    populated_stacks2 = populate_stacks(parsed_list, stacks_list)

    parsed_moves = parse_moves(file)

    final_stacks = make_moves(populated_stacks, parsed_moves)

    final_stacks2 = make_moves2(populated_stacks2, parsed_moves)


    print('PART 1:')
    print(print_message(final_stacks))
    print('PART 2:')
    print(print_message(final_stacks2))    
    

    
