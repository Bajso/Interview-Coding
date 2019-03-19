
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


# 3.) Check whether a sting is balanced (parentheses matching)

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


# 4.) Check if two strings are anagrams

# 4.1) Easiest way is to sort both and compare them
# This is O(nlogn)
def are_anagrams(s1, s2):
    if (sorted(s1) == sorted(s2)):
        return True
    return False

print(are_anagrams('silent', 'listen'))
print(are_anagrams('silent', 'cat'))


# 4.2) Improvement: Count the number of occurances of each character

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


# 4.3) Determine the minimum number of characters to change to make the two substrings into anagrams of one another
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


# 4.4) Minimum Number of Manipulations required to make two Strings Anagram Without Deletion of Character

# Similar to 4.3, but here we use Unicode codes
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


# 5.) Maximum consecutive repeating character in string

# Input: 'geeekk'
# Output: 'e'
def maximum_repeating_char(s):

    max_count = 1
    count = 1
    character = ''
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            count += 1
            if count > max_count:
                max_count = count
                character = s[i]
        else:
            count = 1

    return character, max_count

print(maximum_repeating_char('aaaabbaaaccde'))


# 6.) Is String a Palindrome

# 6.1) Recursive solution
def palindrome_rec(s):

    # base case - if only one character or middle two are the same
    if len(s) == 1 or (len(s) == 2 and s[0] == s[1]):
        return True

    # compare first and last recursively
    if s[0] == s[-1]:
        return palindrome_rec(s[1:-1])
    
    return False

print(palindrome_rec('abcbdefdbcba'))


# 6.2) Iterative solution
def is_palindrome(s):

    for i in range(len(s)//2):
        if not s[i] == s[-(i+1)]:
            return False
        
    return True

print(is_palindrome('abbea'))


# 7.) Remove all consecutive duplicates from string

# Input: abaaccabbbb
# Output: abacab

def remove_consecutive_duplicates(s):

    unique_str = s[0]
    for i in range(len(s) - 1):
        if not s[i] == s[i+1]:
            unique_str += s[i+1]

    return unique_str

print(remove_consecutive_duplicates('abaaccabbbb'))


# 8.) Remove all duplicates from string

# Input: abaaccabbbb
# Output: abc

# Almost always the most efficient way is to use a HashMap implementation since operations are O(1) or O(n) in worst case
def remove_duplicates(s):

    char_dict = dict()
    # populate character dict
    for ch in s:
        if ch not in char_dict.keys():
            char_dict[ch] = 1

    return ''.join(char_dict.keys())

print(remove_duplicates('abaaccabbbb'))