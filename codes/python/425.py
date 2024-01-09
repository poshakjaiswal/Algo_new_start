from typing import List


class Solution:
    answer = []

    def isSquare(self, probable: List[str]) -> bool:

        if len(probable) == 0:
            return False

        if len(probable[0]) != len(probable):
            return False

        count = 0
        for i, i_v in enumerate(probable):

            accumulator = ""

            for j in range(0, len(probable)):
                accumulator = accumulator + probable[j][i]

            if accumulator == probable[i]:
                count += 1

        if count == len(probable):
            print(probable)
            # self.answer.append(probable)
            return True

        return False

    def exploreWordSquare(self, words: List[str], selected: List[str], solve: List[str]):

        if self.isSquare(selected):  # is Solution
            solve.append(selected)
            return

        for word in words:

            if word not in selected:
                selected.append(word)  # pick
                # print(selected)

                self.exploreWordSquare(words, selected, solve)  # backtrack

                selected.remove(word)  # unchoose

        return solve

    def wordSquares(self, words: List[str]) -> List[List[str]]:

        self.exploreWordSquare(words, [], [])

        # print("The solution is :- ")

        # print(self.answer)

        return self.answer


if __name__ == '__main__':
    sol = Solution()
    words = ["area", "lead", "wall", "lady", "ball"]

    # unit test isSquare Method
    test = ["ball", "area", "lead", "lady"]

    # test = ["wall", "area", "lead", "lady"]

    # test = ["lady","area","ball", "lead"]
    # print(sol.isSquare(test))
    print(sol.wordSquares(words))
