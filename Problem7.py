#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?

max = 10001
next = 14
primes = [2,3,5,7,11,13]
counter = len(primes)
checker = 0

while(counter!=max):
    for i in range(0,len(primes)):
        if next%primes[i]==0:
            # not a prime!
            checker = checker + 1
            break

    if (checker==0):
        primes.append(next)
        counter = len(primes)

    next = next + 1
    checker = 0