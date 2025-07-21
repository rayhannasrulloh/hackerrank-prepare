#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    seq_list = [[] for _ in range(n)]
    last_ans = 0
    result = []
    for query in queries:
        q_type, x, y = query
        seq_index = (x ^ last_ans) % n
        if q_type == 1:
            seq_list[seq_index].append(y)
        elif q_type == 2:
            last_ans = seq_list[seq_index][y % len(seq_list[seq_index])]
            result.append(last_ans)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
