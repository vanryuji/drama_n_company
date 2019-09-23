import time

# TODO : 500,000 data?????


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


def compare_similarity(list1, list2):
    return len(list1.intersection(list2)) / 10


if __name__ == '__main__':
    start_time = time.time()

    input_file = '500000.txt'

    input_list = read_input(input_file)
    len_input = len(input_list)

    result = list()
    test_result = list()
    max_similarity = 0
    for i in range(len_input-1):
        for j in range(i+1, len_input):
            similarity = -1
            similarity = compare_similarity(input_list[i], input_list[j])
            if max_similarity <= similarity:
                if max_similarity < similarity:
                    result = list()
                result.append((i, j, similarity))
                test_result.append((i, j, similarity))
                max_similarity = similarity
        if i % 500 == 0:
            print('i:', i)
    print(result)
    print(test_result)

    # TODO : Print result as "1-2, 2-3, 1-3"

    print('elapsed time:', (time.time()-start_time), 's')

