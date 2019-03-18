
# 1.) Reverse a string

text = 'Today is a fine day for Science!'

# 1.1) Reverse using slicing
def reverse_string_slice(s):
    return s[::-1]

print(reverse_string_slice(text))


# 1.2) Reverse manually

# Strings in Python are immutable hence at every loop a copy of output is created character by character,
# hence adding an extra O(n) operation
def reverse_string(s):
    output = ''
    for character in s:
        output = character + output
    return output

print(reverse_string(text))


# 1.3) Reverse manually inplace

# One way to optimise is to create an empty array and add items one by one
def reverse_string_opt(s):
    output_idx = len(s)
    output = [''] * output_idx
    for character in s:
        output[output_idx -1] = character
        output_idx -= 1
    return ''.join(output)

print(reverse_string_opt(text))


# 1.4) Reverse string but keep position of words
def reverse_string_keep_position(s):
    s = s.split(' ')
    output = ''
    for word in s:
        output += word[::-1] + ' '
    return output

print(reverse_string_keep_position(text))


# 2.) Reverse words in a string
def reverse_words(s):
    s = s.split(' ')
    return ' '.join(s[::-1])

print(reverse_words(text))


# 3.) Return missing and mutual values in two lists

# Set is mutable and can only  contain unique values. Standard mathematical functions on sets can be applied
def return_missing_mutual(full_list, partial_list):
    missing_set = set(full_list) - set(partial_list)
    mutual_set = set(full_list).intersection(partial_list)
    return 'Missing: {}\nMutual: {}'.format(missing_set, mutual_set)

print(return_missing_mutual([2,3,4,5,6,7,8,9], [2,4,5,7]))


# 4.) Check whether a sting is balanced (parentheses matching)

# Match every opening bracket to a closing one
def check_balanced_string(s):
    opening_set = ['(', '[', '{']
    closing_set = [')', ']', '}']

    # Construct a dictionary mapping opening to closing brackets
    parentheses_dict = dict(zip(opening_set, closing_set))

    stack = []
    for c in s:
        if c in opening_set:
            # Add matching closing bracket onto the stack
            stack.append(parentheses_dict.get(c))
        elif c in closing_set:
            # Check whether the stack is empty or the closing bracket doesn't match
            if stack == [] or  c != stack.pop():
                return False
        else:
            return False

    # Again check if the stack is empty as they may be unmatched opening brackets left
    if not stack == []:
        return False
    return True

print(check_balanced_string('[()]{}{[()()]}'))
print(check_balanced_string('[()]{}{[()[}'))


# 5.) Maximum product of a triplet in an array (without sorting)

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


# 6.) Check if two strings are anagrams

# 6.1) Easiest way is to sort both and compare them
# This is O(nlogn)
def are_anagrams(s1, s2):
    if (sorted(s1) == sorted(s2)):
        return True
    return False

print(are_anagrams('silent', 'listen'))
print(are_anagrams('silent', 'cat'))


# 6.2) Improvement: Count the number of occurances of each character

# 1. Create a hashmap (a dictionary) where key is character and value is count
# 2. Iterate s1, populate the hashmap and increment the count for repeated characters
# 3. Iterate s2, for each character check if it is present in the hashmap, if not stop. 
# If character is present then decrement count. Also remove element from the hashmap if count is 0
# 4. If hashmap is empty the strings are anagrams, else they are not

def are_anagrams_opt(s1, s2):
    char_dict = dict()

    # Populate the dictionary
    for c in s1:
        if c in char_dict.keys():
            # Update count
            count = char_dict.get(c)
            char_dict[c] = count + 1
        else:
            char_dict[c] = 1
    
    # Check against the other string
    for c in s2:
        if c not in char_dict.keys():
            return False
        elif c in char_dict.keys():
            # Update count
            count = char_dict.get(c)
            # If 1, then next count is 0 and we can remove the element
            if count == 1:
                del char_dict[c]
            else:
                char_dict[c] = count - 1

    # Check whether dictionary is empty
    if bool(char_dict):
        return False
    return True

print(are_anagrams_opt('silent', 'listen'))
print(are_anagrams_opt('silent', 'cat'))


# 6.3) Determine the minimum number of characters to change to make the two substrings into anagrams of one another
def anagram_min_changes(s):

    # if string length is not even it cannot be an anagram
    str_len = len(s)
    if not str_len % 2 == 0:
        return -1

    # split the string
    str_len = int(str_len / 2)
    s1 = s[:str_len]
    s2 = s[str_len:]

    # populate a dictionary
    char_dict = dict()
    for ch in s1:
        # if exists return count, else 0 and increment it
        char_dict[ch] = char_dict.get(ch, 0) + 1

    # check which characters are present in the second string and increment number of changes required
    tot_changes = 0
    for ch in s2:
        # if exist return count, else 0 and decrement it
        count = char_dict.get(ch, 0) - 1
        if count < 0:
            tot_changes += 1
        else:
            char_dict[ch] = count

    return tot_changes

anagram_tests = ['nop', 'xyyx', 'xaxbbbxx', 'fdhlvosfpafhalll']
for test in anagram_tests:
    print(anagram_min_changes(test))


# 6.4) Minimum Number of Manipulations required to make two Strings Anagram Without Deletion of Character

# Similar to 6.3, but here we use Unicode codes
def anagram_count_manipulations(s1, s2):
    
    # store count in a char array 
    char_count = [0] * 25

    count_manipulations = 0

    # iterate through s1 and update count
    for ch in s1:
        # index is Unicode for that character rebased (since 'a' starts at 97)
        index = ord(ch) - ord('a')
        char_count[index] += 1

    # iterate through s2 and update count
    for ch in s2:
        index = ord(ch) - ord('a')
        char_count[index] -= 1

        # if character not found, increase number of manipulations
        if char_count[index] < 0:
            count_manipulations += 1
    
    return count_manipulations

print(anagram_count_manipulations('silent', 'listen'))
print(anagram_count_manipulations('ddcf', 'cedk'))