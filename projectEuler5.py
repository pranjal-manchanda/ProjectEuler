"""
Smallest multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def gcdOfTwo(a, b):
    """
    Input: 2 integers
    Output: Returns gcd of 2 numbers using Euclid's algorithm
    """
    while b:
        a, b = b, a % b
    return a

def lcmOfTwo(a, b):
    """
    Input: 2 integers
    Output: Returns the lcm of 2 numbers using their gcd
    """
    return (a * b) // gcdOfTwo(a, b)

def lcmOfRange(nums):
    """
    Function iteratively applies the lcmOfTwo function to all values in the list
    Output: Returns lcm of the entire list
    """
    # Assign lcm of first 2 numbers to variable
    multiple = lcmOfTwo(nums[0], nums[1])
    for num in range(2, len(nums)): # Iterate through the rest of the list
        multiple = lcmOfTwo(multiple, nums[num]) # Compute new lcm using previous lcm and next value in list
    
    return multiple

# Any number that is a multiple of all numbers between 11-20 is inherently a multiple of all numbers between 1-10. So we only compute LCM of range(11-21)
print(lcmOfRange(range(11, 21)))

"""
Alternatively, could have imported the functools library and applied the reduce function to the list:
print(functools.reduce(lcm, range(1, 20)))
However, my purpose for doing these problems is largely to derive algorithms on my own without importing external libraries. Hence, the lcmOfRange function.
"""