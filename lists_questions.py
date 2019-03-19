
# 1.) Return missing and mutual values in two lists

# Set is mutable and can only contain unique values. Standard mathematical functions on sets can be applied
def return_missing_mutual(full_list, partial_list):
    missing_set = set(full_list) - set(partial_list)
    mutual_set = set(full_list).intersection(partial_list)
    return 'Missing: {}\nMutual: {}'.format(missing_set, mutual_set)

print(return_missing_mutual([2,3,4,5,6,7,8,9], [2,4,5,7]))


# 2.) Maximum product of a triplet in an array (without sorting)

# Input: [10, 3, 5, 6, 20]
# Output: Multiplication of 10, 6 and 20 = 1200

def max_product(arr):
    
    # Get first 3 elements and order them by size (required to avoid if checks)
    subset = arr[0:3]
    # First is largest, then second, then third
    first = subset.pop(subset.index(max(subset)))
    second = subset.pop(subset.index(max(subset)))
    third = subset.pop()

    for i in range(3, len(arr)):
        # if larger than first: swap all
        if arr[i] > first:
            first, second, third = arr[i], first, second
        elif arr[i] > second:
            second, third = arr[i], second
        elif arr[i] > third:
            third = arr[i]

    return first * second * third

print(max_product([10, 3, 5, 6, 20]))


# 3.) Find k smallest items in an array

# One option is to sort the array and pick k smallest, but best case this is O(nlogn) complexity

# To solve it efficiently we can use a MaxHeap
# 1. Create MaxHeap with k items - O(k)
# 2. For every item p in array if p > MaxHeap.getMax() replace max with p - (n-k) * O(logk)
# 3. Print all points from MaxHeap - O(k)

import heapq

def k_smallest_items(arr, k):
    # use inbuilt heap function
    return heapq.nlargest(3, arr)

k_smallest_arr = [1,3,24,5,36,7,85,935,23,8,88]
print(k_smallest_items(k_smallest_arr, 3))
