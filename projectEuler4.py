"""
Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def isPal(i):
    """
    Input: A number cast as a string
    Output: A boolean confirming whether input is a palindrome or not
    Program uses Python's special slicing operator to reverse a string
        Pros: Faster
        Cons: Uses more memory since it creates a shallow copy of the input
    Other possible approaches described at the end of the program
    """
    return i == i[::-1]

def largestPal():
    """
    Input: None
    Output: Largest palindrom number that is a product of two 3-digit numbers
    Program utilizes nested for loops to iterate through all numbers between 999 and 100 to find the largest palindrome
    """
    max, min = 999, 100 #Range for product multiples
    maxPal = 1 #Largest palindrome value found
    for m in range(max, min - 1, -1): #Iterate backwards through 
        for n in range(max, min - 1, -1):
            product = n * m
            if product > maxPal and isPal(str(product)):
                maxPal = product
    return maxPal

print(largestPal())


"""
Different approaches for isPal:
1. Recursion (Probably the slowest)
    # Base case- If string is down to 1 letter, return True
    if len(i) <= 1:
        return True
    # Return equality 
    else:
        return i[0] == i[-1] and isPal(i[1:-1])

2. Reversed:
    return i == "".join(reversed(i))

Different approaches for largestPal():
    Not entirely satisfied with using a brute force solution (even though it's simple and still pretty quick).
    Will try to find a better solution over time.
"""