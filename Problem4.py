# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):

    str_num = str(number)

    length_of_num = len(str_num)

    firsthalf = str_num[0:int(length_of_num/2)]
    secondhalf = str_num[int(length_of_num/2)+1:len(length_of_num)]

    if firsthalf==secondhalf:
        return True

