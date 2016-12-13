# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



# STRATEGY : Every number divisible by 20 is also divisible by 2, 18 by 3, etc...
# Primes in range are... 2,3,5,7,11,13,17,19

# 20 (2,10,5,4), 19, 18 (3,6,2,9), 17, 16 (2,8,4,4), 15 (3,5), 14 (2,7), 13, 12 (2,6,3,4), 11,
# 10 (2,5), 9 (3,3), 8 (2,4), 7, 6 (2,3), 5, 4 (2,2), 3, 2, 1


# 20 (2,4,5,10)
# 19
# 18 (2,3,6,9)
# 17
# 16 (2,4,8)
# 15 (3,5)
# 14 (2,7)
# 13
# 12 (2,3,4,6)
# 11

#just figured it out by hand...

answer = 2520 * 11 * 13 * 17 * 19 * 2

# answer = 232792560