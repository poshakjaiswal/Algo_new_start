import math
from typing import List


# 2 pass solution
def max_pairwise_product(values: List[int]) -> int:  # given array of elements find the max product

    maxPossible = -math.inf
    maxPossibleIndex = -1

    secondBestMaxPossible = -math.inf
    secondBestMaxPossibleIndex = -1

    for i, v in enumerate(values):

        if v >= maxPossible:
            maxPossible = v
            maxPossibleIndex = i

    for i, v in enumerate(values):

        if v >= secondBestMaxPossible and v <= maxPossible and i != maxPossibleIndex:
            secondBestMaxPossible = v
            secondBestMaxPossibleIndex = i

    return values[maxPossibleIndex] * values[secondBestMaxPossibleIndex]


def max_pairwise_product_one_pass(values: List[int]) -> int:  # given array of elements find the max product

    stack = []

    for i, v in enumerate(values):

        if len(stack) < 2:
            stack.append(v)

        else:

            minElement = min(stack[0], stack[1])

            if v >= minElement:
                index = stack.index(minElement)
                stack.pop(index)  # remove one element
                stack.append(v)  # append one element

    return stack[0] * stack[1]


vals = [1, 2, 3]

print(max_pairwise_product(vals))

print(max_pairwise_product_one_pass(vals))
