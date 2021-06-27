###### Fibonacci number
def fibonacci(number):
    '''This function will calculate the fibonacci of the\n
    \rEntery parameter'''

    b = 0
    result = ''
    c = 1
    
    for _ in range(1,number+1):

        while b < number:

            result += str(b) + ","

            b = b+c

            if c < number:

                result += str(c)+ ','

                c = b+c

    if result.endswith(','):
        result = result.removesuffix(',')
    
    return result
