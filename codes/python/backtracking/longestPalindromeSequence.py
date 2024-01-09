
def isPalindrome(inp):
    rev = "".join(reversed(inp))

    if rev == inp:
        return True

    return False

def longestPalndromicSeq(inp ,state ,sol):


    if isPalindrome(state):
        sol.append(state)

        print(state)
        return


    for char in inp:

        if char not in state:

            state.append(char)
            longestPalndromicSeq(inp ,state ,sol)
            state.pop()

def isPalindromeArray(inp :str):

    splitArray = list(inp)

    if "".join(splitArray) == "".join(reversed(splitArray)):
        return True

    return False



def longestPalindromeSequence(inp ,state ,sol):

    if isPalindromeArray(state):

        print(str(state))

        return


    for char in inp:


        state.append(char)

        longestPalindromeSequence(inp, state ,sol)

        state.pop()

    return




if __name__ == '__main__':

    num = "babad"

    # longestPalndromicSeq(num,[],[])

    longestPalindromeSequence(num ,[] ,0)
