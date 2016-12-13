# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):

    # this function only works for numbers with an even number of digits

    str_num = str(number)

    length_of_num = len(str_num)

    firsthalf = str_num[0:int(length_of_num/2)]
    secondhalf = str_num[int(length_of_num/2):length_of_num]

    if firsthalf==secondhalf[::-1]:
        return True
    else:
        return False


def searchSet(test):
    
    for i in range(900,1000):
        if(isPalindrome(test*i)):
            print(test*i)
            break
        if (i==999):
            print("none")


for i in range(900,1000):
    searchSet(i)

