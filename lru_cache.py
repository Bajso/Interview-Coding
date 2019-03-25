
# Web browser design
# Design and implement a web browser, which supports the functionality that at any given instance
# you can efficiently tell the top 5 visited web pages on basis of the number of visits. The question is a variant of a LRU cache.

# Least Recently Used (LRU) Cache can be optimally implemented using a hashmap and a doubly linked list or a priority queue

# Hashmap maps the URLs to the number of visits, which are maintained with a priotiry queue. HashMap (dict) has O(1) time for 
# inserting/searching if a webpage was visited earlier and a priority queue ensures that only top k elements are stored.
# Priority queue can be implemented with max or min heap, as remove max/min is always O(1), since we are removing the root. Since heap
# is a complete binary tree sorting it takes O(logn) in worst case.

# In Python we can use a dictionary and check for n largest values in a dictionary with heapq built-in module
# heapq.nlargest(10, my_dictionary.values())


