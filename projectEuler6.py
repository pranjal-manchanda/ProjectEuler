"""
Sum square difference

Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def diffSquares(n):
    """
    Input: Integer value
    Output: Difference between sum of first n numbers squared and sum of the squares of the first n numbers
    """
    sqOfSum, sumOfSq, difference = 0, 0, 0
    # Calculate sum of first n natural numbers
    for i in range(n + 1):
        sqOfSum += i
    
    sqOfSum **= 2

    # Calculate sumOfSq using summation formula
    sumOfSq = ((n**3)/3) + ((n**2)/2) + (n/6)

    # Calculate difference
    difference = sqOfSum - sumOfSq
    return difference

print(diffSquares(100))