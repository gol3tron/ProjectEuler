#The sum of the squares of the first ten natural numbers is,
#
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def squaresum(max_num):
    
    # add up all the numbers from 1 to max_num and square them
    # formula due to CF Gauss. What a guy!

    return (max_num*(max_num + 1)/2)**2

def sumsquares(max_num):

    # add up all the squares from 1 to max_num and add them
    
    num_sequence = list(range(1,max_num+1))

    return sum([i ** 2 for i in num_sequence])

print(abs(sumsquares(100)-squaresum(100)))