from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        min_capacity = max(weights)

        total_possible = sum(weights)

        start = 0
        count = 0

        for i in range(min_capacity, total_possible):

            accumulator = i

            for j in range(start, len(weights)):

                if ((accumulator - weights[j]) < 0):
                    start = j
                    count = count + 1


                else:
                    accumulator = accumulator - weights[j]

            if count == days:

                return i

            else:
                count = 0
                start = 0

        return 0




if __name__ == '__main__':

    sol = Solution()
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5

    print(sol.shipWithinDays(weights,days))




