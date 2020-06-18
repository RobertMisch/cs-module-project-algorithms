'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #dosent quite work, hangs up on duplicate 0's
    # for index, number in enumerate(arr):
    #     # print (f"our arr: {arr} index being checked:{index} number:{number}")
    #     if number == 0:
    #         arr.pop(index)
    #         arr.append(0)
    # return arr
    for i in range(len(arr)-1, -1, -1):
        # print(arr[i])
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")