
def subsetSum(choices,state,current_total,target,res: list[list[int]]):

    if current_total == target :
        res.append(list(state))
        print(state)
        return

    for choice in choices:

        if current_total + choice > target:
            continue

        state.append(choice)#make a choice

        subsetSum(choices,state,current_total+choice,target,res) # backtrack

        #state.pop()
        state.remove(choice)



def subsetSum1(choices, states,target):

    if sum(states) == target :
        print(states)
        return

    for choice in choices:


        states.append(choice)#make a choice

        subsetSum(choices,states,target) # backtrack

        states.remove(choice)


    return


if __name__ == "__main__":

    nums = [3,4,5]
    target = 9
    res= []

    subsetSum(nums,[],0,target,res)

    print(res)

