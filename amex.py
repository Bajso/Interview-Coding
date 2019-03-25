
def coin_count(coin_list, sum):
    
    # Ensure list is sorted in descending order
    coin_list.sort(reverse=True)
    
    if not coin_list or sum == 0:
        return [0]

    coin_cache = list()

    i = 0
    size = len(coin_list)
    while i <  size:
        if coin_list[0] <= sum:
            sum -= coin_list[0]
            coin_cache.append(coin_list[0])
        else:
            coin_list.pop(0)
            i += 1

    if sum > 0:
        return [0]

    return coin_cache


print(coin_count([20, 10, 5, 1], 53))