def count_sort(arr, maximum=None):
    # Your code here
    #we need to build an array for each number up to our maximum
    if len(arr)==0:
        return arr
    if maximum==None:
        maximum=0
        for number in arr:
            if number > maximum:
                maximum=number
    count_arr=[] 
    sorted_arr=[]
    for i in range(len(arr)):
        sorted_arr.append(0)
    for i in range(maximum+1):
        count_arr.append(0)
    for number in arr:
        if number >=0:
            count_arr[number]+=1
        else:
            # print("Error, negative numbers not allowed in Count Sort")
            return "Error, negative numbers not allowed in Count Sort"
    for index in range(1, len(count_arr)):
        count_arr[index] = count_arr[index] + count_arr[index-1]
    #so we need to look at our original array value
    #we check the count_arr[og value]
    #whatever number is stored in that index, is the correct placement of the og value
    #then we subtract 1 from the count on the count_arr[og value]
    #then we move to the next index in our og array

    for number in arr:
        sorted_arr[count_arr[number]-1] = number
        count_arr[number]-=1

    return sorted_arr

'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # so we need to take a list, and find a single value in that list
    #we could create a flag system, similar to count sort and the primes algorithm
    #we'll find the maximum value in the list
    #these flags will indicate which values have duplicates

    #finding the max value
    max_value=0
    for number in arr:
        if number > max_value:
            max_value=number
    
    #flag system initialization
    flags=[]
    for i in range(max_value+1):
        flags.append(0)
    #then we need to mark the values as counted. the value is the index on flags
    for number in arr:
        flags[number]+=1
    #search through flags to see what has only 1 entry
    for index, flag in enumerate(flags):
        if flag == 1:
            return index

    
    



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")