#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math


for b in range(5,1000):
    for a in range(4,b):
        test_c = math.sqrt(a**2 + b**2)

        if (test_c%int(test_c)==0):
            
            c = test_c
            
            if (a + b + c == 1000):
                solution = a*b*c
                print("a is :"+str(a))
                print("b is :"+str(b))
                print("c is :"+str(c))
                print("solution is :"+str(solution))
                break


