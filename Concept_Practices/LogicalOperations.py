# !/usr/bin/env python3

# This is a practice file for logical operations in Python.
# Logical operations combine boolean values to produce a new boolean value.
# The three main logical operators are:
# and (logical AND), or (logical OR), and not (logical NOT).

# The and operator returns True if both operands are True.
a = True
b = False
print("a and b:", a and b)     # False, because b is False

# The or operator returns True if at least one operand is True.
print("a or b:", a or b)      # True, because a is True

# The not operator negates the boolean value.
print("not a:", not a)      # False, because a is True
print("not b:", not b)      # True, because b is False

# Logical operators and math
var = 1
print(var> 0)
print(not (var<= 0))
print(var != 0)
print(not (var == 0))

# De Morgan's Laws
# The negation of a conjunction (and) is equivalent to the disjunction (or) of the negations.
not (a and b) == (not a) or (not b)  # True
# The negation of a disjunction (or) is equivalent to the conjunction (and) of the negations.
not (a or b) == (not a) and (not b)  # True

# Bitwise logical operations
# Bitwise operations can also be used with boolean values.
# The & operator performs a bitwise AND operation.
print("a & b:", a & b)      # False, because b is False
# The | operator performs a bitwise OR operation.
print("a | b:", a | b)      # True, because a is True
# The ^ operator performs a bitwise XOR operation.
print("a ^ b:", a ^ b)      # True, because a is True and b is False
print("b ^ a:", b ^ a)      # True, because b is False and a is True
# The ~ operator performs a bitwise NOT operation.
print("~a:", ~int(a))      # -2, because ~True is -2 in two's complement representation
# According to the run, ~BOOL is going to be deprecated, hence the int() conversion.

# Logical vs Bitwise Operations
i = 15
j = 22
print('log i and j:', i and j)  # 22, because both are non-zero
print('bit i and j:', i & j)     # 6, because 15 & 22 = 01111 & 10110 = 00110
print('bitneg i:', ~i)  # -16, because ~15 = -16 in two's complement representation

# Binary Shift Operations
# Binary shift operations can also be used with integers.
# The << operator performs a left shift operation.
print("i << 1:", i << 1)  # 30, because 15 << 1 = 1111 becomes 11110
# The >> operator performs a right shift operation.
print("i >> 1:", i >> 1)  # 7, because 15 >> 1 = 1111 becomes 0111
