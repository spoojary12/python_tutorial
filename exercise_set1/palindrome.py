def palindrome_checker(num):
    '''
     This function checks if a number is a palindrome
     @params : num <int>
     @return boolean
    '''
    #1. Reverse the original number
    #1a. convert the number into a string
    num_string = str(num)
    #1b. Reverse
    num_reverse = num_string[::-1]
    #2. compare both reversed and original string
    isPalindrome =  num_reverse == num_string
    #3. return the boolean True if palindrom, False if not palindrome
    return isPalindrome


print(palindrome_checker(122))