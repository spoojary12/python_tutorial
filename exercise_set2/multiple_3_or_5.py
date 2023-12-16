'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000

'''

def sum_of_multiples(num):
    '''
    @params maxvalue <int>
    @returns sum <int>
    '''
    sum = 0
    #step1 Iterate max_value time
    for i in range(num):
        #step2 check if divisible by 3 or 5
        is_divisible =is_div_by(i, 3, 5)
        if is_divisible:
            #step3 if divisible then add to sum
            sum = sum + i
    return sum


def is_div_by(original, num1, num2):
    '''
    @param num1 <int>
    @param num2 <int>
    @returns boolean
    
    '''
    remainder1 = original % num1
    remainder2 = original % num2
    return (remainder1 == 0) or (remainder2 == 0)
        



print(sum_of_multiples(1000))