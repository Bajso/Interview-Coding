
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