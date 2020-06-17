'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    #so I'm going to go about this in a Tri-nary fashion
    #initialize the bytes 
    register=[]
    total=1
    for i in range(n):
        register.append(1)

def permintations():
    pass


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    #draw out what the answer should be
    """
    total permintations
    1,1,1,1,1
    1,1,1,2
    1,1,2,1
    1,2,1,1
    2,1,1,1
    2,1,2
    2,2,1
    1,1,3
    1,3,1
    3,1,1
    2,3
    3,2
    """

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
