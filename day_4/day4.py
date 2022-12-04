print('Enter filename')
filename = 'i2.txt' # input()

def form_pairs(list):
    new_list = []
    new_list2 = []
    for string in list:
        new_list.append(string.split(','))

    for string in new_list:
        to_append = []
        for pairs in string:
            to_append.append(pairs.split('-'))
        new_list2.append(to_append)
    return new_list2

def is_fully_contained(s1, s2):
    return int(s1[0]) >= int(s2[0]) and int(s1[1]) <= int(s2[1]) or int(s2[0]) >= int(s1[0]) and int(s2[1]) <= int(s1[1])

def is_overlapping(s1, s2):
    return is_fully_contained(s1,s2) or int(s1[1]) >= int(s2[0]) and int(s1[1]) <= int(s2[1]) or int(s2[1]) >= int(s1[0]) and int(s2[1]) <= int(s1[1])

with open(filename) as f:
    containCount = 0
    overlapCount = 0
    cleanup_sections = f.read().splitlines()
    parsed_pairs = form_pairs(cleanup_sections)
    for pairs in parsed_pairs:
        print(pairs)
        if is_fully_contained(pairs[0], pairs[1]):
            containCount += 1
        if is_overlapping(pairs[0], pairs[1]):
            overlapCount += 1
    print('PART 1:\n' + str(containCount))
    print('PART 2:\n' + str(overlapCount))