
def candies_and_wrappers():
    m, n, p, q = [int(i) for i in input("Please enter m, n, p, q: ").split()]
    n * m

def maxCandyCount(candy_per_ringgit, min_wrappers_count, exchange_candy_count, money):
    # initialize variables, separating candy and wrapper count
    candy_in_hand = money * candy_per_ringgit
    wrapper_in_hand = candy_in_hand

    # loop until no more wrapper can be exchanged for new candies
    while wrapper_in_hand >= min_wrappers_count:

        # calculate the maximum number of exchanges possible and
        # total candy that can be exchanged
        times_can_be_exchanged = wrapper_in_hand // min_wrappers_count
        new_candy_exchanged = exchange_candy_count * times_can_be_exchanged
        
        # deduct used wrappers from wrapper in hand
        used_wrapper = min_wrappers_count * times_can_be_exchanged
        wrapper_in_hand -= used_wrapper
        
        # add newly aquired candies to hand (candy itself and the wrapper)
        candy_in_hand += new_candy_exchanged
        wrapper_in_hand += new_candy_exchanged

    return candy_in_hand

def maxCandyCountRecursive(candy_per_ringgit, min_wrappers_count, exchange_candy_count, money=0, candy_in_hand=0, wrapper_in_hand=0):
    if money and candy_in_hand == wrapper_in_hand == 0:
        candy_in_hand = money * candy_per_ringgit
        wrapper_in_hand = candy_in_hand
        
    if wrapper_in_hand < min_wrappers_count: return candy_in_hand
    
    times_can_be_exchanged = wrapper_in_hand // min_wrappers_count
    new_candy_exchanged = exchange_candy_count * times_can_be_exchanged
    
    used_wrapper = min_wrappers_count * times_can_be_exchanged
    wrapper_in_hand -= used_wrapper
    
    candy_in_hand += new_candy_exchanged
    wrapper_in_hand += new_candy_exchanged

    return maxCandyCountRecursive(candy_per_ringgit, min_wrappers_count, exchange_candy_count, money, candy_in_hand, wrapper_in_hand)
print(maxCandyCount(2, 1, 3, 1))