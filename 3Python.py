"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
num = 600851475143
largestPrime = 0

# If number is even, then its largest prime factor will be 2. We can exit the program.
# Else, set largest prime factor to None initially and proceed onwards with program.
if num % 2 == 0:
    largestPrime = 2
    print(largestPrime)
    exit()
else:
    largestPrime = None

# We have already checked if 2 is a factor and there is no other prime even number so we can simply iterate through only the odd numbers
# We iterate only up to the square root of num (Reasons explained in comments at the end of program)
for i in range(3, int(num ** (1/2.0)), 2):
    # If num divisible by i, flag i as a factor
    if num % i == 0:
        flag = True
        # If i is even, flag it as not a prime factor and move on to the next iteration of i
        # Else check if it is prime by iterating through all odd numbers up to square root of i to see if i has any factors (or it is prime)
        if i % 2 == 0:
            flag = False
            break
        else:
            for j in range(3, int(i ** (1/2.0)), 2):
                if i % j == 0:
                    flag = False
                    break
        # If flag is true, we know that i is a prime factor of num so we set that as the largestPrime we have found thus far
        if flag:
            largestPrime = i
            #print(i)
# Print the largestPrime found at the end of the computation above
print(largestPrime)

"""
Explanation for why we only iterate up to the square root of num:
    Suppose n = a * b,
    Now, if a and b were both greater than sqrt(n),then a * b > n. So that is not possible.
    So at least one of a or b must be equal to, or less than, sqrt(n) aka min(a,b) <= sqrt(n)
    Therefore, if we can iterate through all numbers up to min(a,b), we can check if n has any factors (ie is it prime or not)
"""