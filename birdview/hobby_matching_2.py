import time
import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform


def read_input(input_file):
    result = list()
    with open(input_file) as f:
        for i, line in enumerate(f):
            hobbies = line.strip().split(' ')
            if len(hobbies) != 10:
                # It's not a hobby
                continue
            tmp = [0] * 26
            for hobby in hobbies:
                idx = ord(hobby) % 65  # 65 means 'A'
                tmp[idx] = 1
            result.append(tmp)
    return result


if __name__ == '__main__':
    start_time = time.time()

    input_file = '500000.txt'
    input_list = read_input(input_file)
    print('elapsed time, after reading input:', (time.time() - start_time), 's')

    df = pd.DataFrame(np.array(input_list))
    print('elapsed time, after creating df:', (time.time() - start_time), 's')
    dist_matrix = pdist(df, metric='euclidean')
    print('elapsed time, after creating pdist:', (time.time() - start_time), 's')
    row_dist = pd.DataFrame(squareform(dist_matrix))
    print('elapsed time, after creating row_dist:', (time.time() - start_time), 's')
