# Find the Largest of 2 numbers and print the largest one
# a = 10, b= 20

# Print the largest b
a = 10
b = 20
if a > b:
    print(a)
else:
    print(b)

print('===========================================================================')
# Print the largest a
a = 20
b = 10
if a > b:
    print(a)
else:
    print(b)

print('===========================================================================')
# Printing number along with variable name
a = 20
b = 10
if a > b:
    print('a: ', a)
else:
    print('b: ', b)
print('===========================================================================')
# Getting input form user
a = int(input())
b = int(input())
if a > b:
    print('a: ', a)
else:
    print('b: ', b)
print('===========================================================================')
# Test case coverage equals => if if else
if a == b:
    print('a and b are equal')
if a > b:
    print('a: ', a)
else:
    print('b: ', b)
print('===========================================================================')
# Test case coverage equals => if elif else
if a == b:
    print('a and b are equal')
elif a > b:
    print('a: ', a)
else:
    print('b: ', b)
print('===========================================================================')

# Output 
# File://problem_solving/largest-num.py
# 67
# 76
# b:  76

# File://problem_solving/largest-num.py
# 65
# 87
# b:  87

# File://problem_solving/largest-num.py
# 0 
# 1
# b:  1

# File://problem_solving/largest-num.py
# 1
# 0
# a:  1

# File://problem_solving/largest-num.py
# 10
# 10
# b:  10

# File://problem_solving/largest-num.py
# 0
# 0
# b:  0

# File://problem_solving/largest-num.py
# -10
# +10
# b:  10

# File://problem_solving/largest-num.py
# -10
# -20
# a:  -10

# File://problem_solving/largest-num.py
# hi
# Traceback (most recent call last):
#   File "c:\Users\NayeemJohnY\MySpace\Yaseer\problem_solving\largest-num.py", line 8, in <module>
#     a=int(input())
# ValueError: invalid literal for int() with base 10: 'hi'

# File://problem_solving/largest-num.py
# 10
# 10
# a and b are equal
# b:  10

# File://problem_solving/largest-num.py
# 10
# 10
# a and b are equal

# File://problem_solving/largest-num.py
# 10
# 20
# b:  20

# File://problem_solving/largest-num.py
# 20
# 10
# a:  20