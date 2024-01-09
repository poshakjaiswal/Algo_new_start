from typing import List


class Solution:

    def isStrobogrammatic(self, num: str) -> bool:

        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}

        rotated_string_builder = []

        for c in reversed(num):
            if c not in rotated_digits:
                return False
            rotated_string_builder.append(rotated_digits[c])

        rotated_string = "".join(rotated_string_builder)
        return rotated_string == num

    def strobogram(self, n: int, output):

        if n == 0:
            output.append("")
            return

        elif n == 1:
            output.append("0")
            output.append("1")
            output.append("8")
            return
        elif n == 2:
            output.append("11")
            output.append("69")
            output.append("88")
            output.append("69")
            return

        while n > 0:
            n = n - 1

            self.strobogram(n, output)

    def findStrobogrammatic(self, n: int) -> List[str]:

        output = []
        n = 2
        self.strobogram(n, output)

        print(output)

        pass


if __name__ == "__main__":
    sol = Solution()
    sol.findStrobogrammatic(1)
