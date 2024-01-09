
def permuteArray(choices ,state ,answer):

    if  len(state) == 3 :

        print(state)
        answer.append(state)
        return



    for choice in choices:

        if choice not in state:
            state.append(choice)
            permuteArray(choices ,state ,answer)
            state.remove(choice)




if __name__ == "__main__":

    nums = [1 ,2 ,3]

    permuteArray(nums,[],[])
