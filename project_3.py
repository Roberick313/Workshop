###### Factorial number

def my_factorial(num=0):
    '''this function will retunr the factorial of the entery parameter\n
    \rand have a defult parameter in case that it doesnt get any parameter.'''
    
    storage = 1
    counter = 1

    f= open('My_factorial.txt','w')
    f.write('')
    f.close()

    if num:
        while counter <= num:
            storage *= counter
            counter += 1
        return f'the factorial of {num} is {storage}' 
    else:
        num = [2,3,5,8,9]
        for i in num:
            
            while counter <= i:
                storage *= counter
                counter += 1

            f= open('My_factorial.txt','a')
            f.write('the factorial of: '+str(i)+' '+'is'+' '+str(storage)+'\n')
            f.close()

        return open('My_factorial.txt').read()

print(my_factorial(50000))
