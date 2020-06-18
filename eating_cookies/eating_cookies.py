'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
    # if(n==0):
    #     return 1
    # elif(n==1):
    #     return 1
    # elif(n==2):
    #     return 2
    # elif(n==3):
    #     return 4
    # else:
    #     total=(eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))
    #     return total
    #prof first pass solution run time for this, and mine is 3^n. aka big bad
    # if n<0:
    #     return 0
    # elif n==0:
    #     return 1
    # else:
    #     return (eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))
    #however, all these recursive calls are actually redundant, that's what makes it so slow
    #we can resolve this by using a cache
    #what's a cache? it saves our work, so we dont ever do redundant work "lets you save the game"
    #a cache is a dictionary whrer the keys is the n, value is the answer
def eating_cookies(n, cache):
    #just because we are using the cache dosent change the equation. but we need more logic
    if n<0:
        return 0
    elif n==0:
        return 1
    elif cache[n] > 0:
        return cache[n]
    else:
        #otherwise out cache dosent contain the answer, so we calc it.
        #then save answer in cache
        cache[n]=(eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache))
        return cache[n]
    #this shaves it down to just O(n)


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
    cache=[0 for i in range(num_cookies+1)]
    print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to each {num_cookies+1} cookies")

#teacher code
# Runtime: O(3^n)
# def eating_cookies(n):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:
#         return eating_cookies(n-3) + eating_cookies(n-2)+ eating_cookies(n-1)
# the cache allows us to save our work 
# cache is a dictionary where keys is the n, value is the answer 
# Runtime: O(n)
# def eating_cookies(n, cache):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     # check if the answer is in our cache 
#     elif cache[n] > 0:
#         return cache[n]
#     else:
#         # otherwise, our cache doesn't contain the answer, so we'll use our 
#         # recursive logic to calculate it, and then save the answer in our 
#         # cache for future uses 
#         cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache)+ eating_cookies(n-1, cache) 
#     return cache[n]
# ​
# ​
# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 100
#     cache = {i: 0 for i in range(num_cookies+1)}
#     print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to each {num_cookies} cookies")