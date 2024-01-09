def isPalindromeArray(inp: str):
    splitArray = list(inp)
    return "".join(splitArray) == "".join(reversed(splitArray))


def longestPalindromeSequence(inp, state, sol):
    if isPalindromeArray(state):
        if len(state) > len(sol[0]):
            sol[0] = state[:]
        return

    for char in inp:
        state.append(char)
        longestPalindromeSequence(inp, state, sol)
        state.pop()

    return sol

if __name__ == '__main__':
    num = "babad"
    longest_palindrome = []
    longestPalindromeSequence(num, [], [longest_palindrome])
    print("Longest Palindromic Substring:", "".join(longest_palindrome))
