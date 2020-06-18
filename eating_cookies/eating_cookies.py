'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # if(n<=2):
    #     return 0
    # elif(n==3):
    #     return 1
    # else:
    #     total=(eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))
    #     return total
    myArr=[1]
    answer=0
    for i in range(n):
        total=0
        # total+=myArr[i]
        # if i>=0:
        #     total+=1
        if i>=1:
            total+=myArr[i-1]
        if i>=2:
            total+=myArr[i-2]
        if i>=3:
            total+=myArr[i-3]
        myArr.append(total)
    for num in myArr:
        answer+=num
    return answer



if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    #draw out what the answer should be
    """
    total permintations
    1

    1,1
    2

    111
    12
    21

    3

    1111
    112
    121
    211
    22

    13
    31

    5
    1,1,1,1,1
    1,1,1,2
    1,1,2,1
    1,2,1,1
    2,1,1,1
    1,2,2
    2,1,2
    2,2,1

    1,1,3
    1,3,1
    3,1,1
    2,3
    3,2

    6
    1,1,1,1,1,1
    1,1,1,1,2
    1,1,1,2,1
    1,1,2,1,1
    1,2,1,1,1
    2,1,1,1,1
    1,1,2,2
    1,2,1,2
    2,1,1,2
    2,1,2,1
    2,2,1,1
    2,2,2
    """

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
