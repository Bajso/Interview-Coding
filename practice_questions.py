
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