from collections import deque
from typing import List


class Solution:
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def isValidMove(self, dir, m, n):

        row = dir[0]
        col = dir[1]

        if row >= 0 and col >= 0:

            if row < m and col < n:
                return True

        return False

    def dfs(self, board: List[List[str]], word: str, start_row, start_col) -> bool:

        stack = []
        visited = set()

        m = len(board)
        n = len(board[0])

        stack.append((start_row, start_col))

        accumulator = []

        accumulator.append(board[start_row][start_col])

        while stack:

            current = stack.pop()

            if current not in visited:
                visited.add(current)
                # accumulator.append(board[current[0]][current[1]])
                print(current)
                print((board[current[0]][current[1]]))

                for dir in self.directions:

                    new_dir = (current[0] + dir[0], current[1] + dir[1])

                    if self.isValidMove(new_dir, m,
                                        n):  # we can take a greedy approach by favouring the path which realizes our word faster
                        if new_dir not in visited:
                            stack.append(new_dir)

        return False

    def exist1(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])

        found = self.dfs(board, word, 0, 0)

        if found:
            return True

        # for i in range(0,m):
        #     for j in range(0,n):
        #         if board[i][j] == word[0]:
        #
        #             found = self.dfs(board,word,i,j)
        #
        #             if found:
        #                 return True

        return False

    def isSolution(self, states, target_word,board):
        word = ""

        for cord in states:
            word = word + str(board[cord[0]][cord [1]])

        print(word)
        return word == target_word

    def backTrack(self, states, target_word, result,board):

        if self.isSolution(states, target_word,board):
            result = True
            return

        current = states.pop()
        for dir in self.directions:

            new_dir = (current[0] + dir[0], current[1] + dir[1])

            if self.isValidMove(new_dir, 3, 4) :
                states.append(new_dir)

                self.backTrack(states, target_word, result,board)

                states.pop()

    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        self.backTrack([(0, 0)], word, result,board)

        return  result


# perform BFS


if __name__ == "__main__":
    sol = Solution()

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    print(sol.exist(board, word))
