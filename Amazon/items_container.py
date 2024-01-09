#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numberOfItems' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY startIndices
#  3. INTEGER_ARRAY endIndices
#

def containers(s):
    compartments = dict()

    prefix_compartment = dict()

    previous = 0
    pipes = set()

    for i, v in enumerate(s):

        count = 0
        temp = i
        flag = False

        if v == "|":  # marking start of one compartment

            while temp < len(s):
                temp = temp + 1
                count = count + 1
                if temp < len(s) and s[temp] == "|":
                    flag = True
                    break

            if flag:
                pipes.add(i)
                pipes.add(temp)
                compartments[(i, temp)] = count - 1

                prefix_compartment[temp] = previous + count - 1

                previous = count - 1

    # print(compartments)
    # print(prefix_compartment)

    return pipes, prefix_compartment


def numberOfItems(s, startIndices, endIndices):
    pipes, prefix_compartment = containers(s)
    print(pipes)
    print(prefix_compartment)

    output = []

    for i, v in enumerate(startIndices):

        candidate = [v - 1, endIndices[i] - 1]

        left_pointer = candidate[0]
        right_pointer = candidate[1]

        print("left_pointer",left_pointer)
        print("right_pointer",right_pointer)

        while right_pointer >= 0:  # nearest pipe
            if right_pointer in pipes:

                break
            else:

                right_pointer = right_pointer - 1

        while left_pointer < right_pointer and left_pointer >= 0 and right_pointer > 0:  # nearest pipe
            if left_pointer  in pipes:
                break

            else:

                left_pointer = left_pointer + 1
        print("revised_left",left_pointer)
        print("revised_right",right_pointer)

        if left_pointer + 1 < right_pointer :

            left_obj = 0

            if left_pointer + 1 in prefix_compartment:
                left_obj = prefix_compartment[left_pointer + 1]

            output.append(prefix_compartment[right_pointer ] - left_obj)
        else:
            output.append(0)

    return output

    # Write your code here
if __name__ == '__main__':

    s= '|**|*|*'
    startIndices = [1,1]
    endIndicies = [5,6]

    print(numberOfItems(s,startIndices,endIndicies))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     startIndices_count = int(input().strip())
#
#     startIndices = []
#
#     for _ in range(startIndices_count):
#         startIndices_item = int(input().strip())
#         startIndices.append(startIndices_item)
#
#     endIndices_count = int(input().strip())
#
#     endIndices = []
#
#     for _ in range(endIndices_count):
#         endIndices_item = int(input().strip())
#         endIndices.append(endIndices_item)
#
#     result = numberOfItems(s, startIndices, endIndices)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
