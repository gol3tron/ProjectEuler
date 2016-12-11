#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


def getPrimes(n):
    for p in range(2, n+1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            print(p),
    print('Done')

def factorize(m,n):

    for p in range(2, n+1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            if m % p == 0:
                print(p)


