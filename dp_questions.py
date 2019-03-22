# 1.) Fibonacci Sequence

# 0,1,1,2,3,5,8
def fibonacci(n):
    
    # 1.1) Recursive Solution
    def fib_recursive(n):
        # Base case
        if n < 2:
            return n
        # Recursive step
        else:
            return fib_recursive(n-1) + fib_recursive(n-2)

    # Time complexity of recursive solution is T(n) = T(n-1) + T(n-2), which is O(2^n)

    # 1.1) DP Solution

    # Many recursive solutions can be optimised by storing overlapping subproblems at each recursive call
    # This is called Memoisation
    mem = dict()
    def fib_dp(n, mem):

        if n in mem:
            return mem[n]

        # Base case
        if n < 2:
            return n
        # Recursive step
        else:
            mem_value = fib_dp(n-1, mem) + fib_dp(n-2, mem)
            mem[n] = mem_value
            return mem[n]

    print(fib_recursive(n))
    print(fib_dp(n * 100, mem))

fibonacci(5)


# 2.) Coin Change

# Given a value N, if we want to make change for N cents, and we have an infinite supply of each of S={S1,S2,..,Sm} 
# valued coins, how many ways can we make the change? The order of coins does not matter

# Questions to ask before solving:
# - duplicates in supply array
# - is the supply array sorter
# - negative N or supply with coins with negative value

# Input: N (sum), S (coin supply)
# Output: Number of combinations

# 1. Determine all possible subsets from coin supply and keep all that add up to N
# 2. Break down the original problem into smaller subproblems
# - let's call the number of subsets that add up to N, n
# - n = (number of subsets with largest supply coin) + (number of subsets without largest supply coin)

# 4.1) Pure recursive solution with exponential time due to overlapping subproblems
def coin_change_recursive(N, S):   

    # Determines the amount of subsets that add up to sum but only considering coins up to idx
    def make_change(supply, sum, idx):
        
        # Base cases
        # 1. There is only one way to get sum = 0, which is by using no coins
        if sum == 0:
            return 1
        # 2. If sum is negative, then no solution exists
        elif sum < 0:
            return 0
        # 3. If there are no coins and sum is greater than 0, then no solution exists
        elif idx < 0 and sum >= 1:
            return 0

        # Recursive calls
        # (number of subsets without largest supply coin) + (number of subsets without largest supply coin)
        else:
            return make_change(supply, sum, idx - 1) + make_change(supply, sum - supply[idx], idx)

    return make_change(S, N, len(S) - 1)

print(coin_change_recursive(4, [1, 2, 3]))


# 4.2) Memoised solution - Dynamic Programming
def coin_change_dp(N, S):   

    memory = dict()

    # Function takes in memory as well
    def make_change(supply, sum, idx, mem):

        # As key has to be unique we can combine current sum with index
        key = '{}-{}'.format(sum, idx)

        if key in mem:
            return mem[key]
        
        if sum == 0:
            return 1
        elif sum < 0:
            return 0
        elif idx < 0 and sum >= 1:
            return 0
        else:
            # Store in memory for faster lookup
            mem_value = make_change(supply, sum, idx - 1, mem) + make_change(supply, sum - supply[idx], idx, mem)
            mem[key] = mem_value
            return mem[key]

    return make_change(S, N, len(S) - 1, memory)

print(coin_change_dp(4, [1, 2, 3]))