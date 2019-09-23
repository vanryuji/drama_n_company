def read_input(input_file):
    result = list()
    with open(input_file) as f:
        for i, line in enumerate(f):
            hobby = line.strip().split(' ')
            if len(hobby) != 10:
                # It's not a hobby
                continue
            result.append(set(hobby))
    return result


input_list = read_input('test.txt')
for i in range(4):
    for j in range(i+1, 5):
        print(i, j)
        print(input_list[i].intersection(input_list[j]))