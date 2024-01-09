class Solution:
    directions = [(0, 1),  # right
                  (0, -1),  # left
                  (-1, 0),  # up
                  (1, 0),  # down

                  (1, 1),  # digonal right
                  (1, -1),  # diagonal left
                  (-1, -1),  # diagonal up left
                  (-1, 1)  # down up right

                  ]

    possible = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    skip_path = dict()
    skip_path[(1, 7)] = 4
    skip_path[(1, 3)] = 2
    skip_path[(1, 9)] = 5
    skip_path[(2, 8)] = 5
    skip_path[(3, 7)] = 5
    skip_path[(3, 9)] = 6
    skip_path[(4, 6)] = 5
    skip_path[(7, 9)] = 8

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    paths = set()

    # def backTrack(self,choices,state,answer,steps):
    #     if steps == 1:
    #         answer.append(["0","1","2","3","4","5","6","7","8","9"])
    #         return
    def convertToPattern(self, listOfTuples) -> str:

        curr = []

        for i in listOfTuples:
            curr.append(str(self.matrix[i[0]][i[1]]))

        return "".join(curr)

    def dfs(self, start_i, start_j, moves):

        visited = set()
        stack = []

        stack.append((start_i, start_j))

        while stack :

            current = stack.pop()

            temp_path= []
            temp_path.append(current)

            print(current)

            for dir in self.directions:
                if moves > 0:
                    take_one_step = (dir[0] + current[0], dir[1] + current[1])
                    if take_one_step not in visited and take_one_step in self.possible:
                        stack.append(take_one_step)
                        temp_path.append(take_one_step)
                        visited.add(take_one_step)
                        #moves = moves - 1
            self.paths.add(self.convertToPattern(temp_path))

    def numberOfPatterns(self, m: int, n: int) -> int:

        for moves in range(m, n):
            for j in range(0, 3):
                for k in range(0, 3):
                    self.dfs(j, k, moves)

        print(self.paths)

        return len(self.paths)


if __name__ == "__main__":
    sol = Solution()

    m = 1
    n = 2

    print(sol.numberOfPatterns(m, n))
