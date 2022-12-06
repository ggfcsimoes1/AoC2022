print('Enter filename')
filename = input()


def is_marker(string):
    return len(set(string)) == len(string)

def find_marker(string, pattern_size):
    i=pattern_size
    while not is_marker(string[i-pattern_size:i]):
        i+=1
    return i

with open(filename) as f:

    file = f.read().splitlines()

    print('INPUT')
    print('-----')
    print(file[0])
    print('-----')
    print('PART 1:')
    print(find_marker(file[0], 4))
    print('PART 2:')
    print(find_marker(file[0], 14))
    

    
