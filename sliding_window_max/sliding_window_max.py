import collections
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # my_queue= collections.deque()
    answer=[]
    for i in range(len(nums)-(k-1)):
        slide=nums[i:i+(k)]
        # print(slide)
        window_max=nums[i]
        for num in slide:
            if num > window_max:
                window_max=num
        answer.append(window_max)
    return answer
            




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
