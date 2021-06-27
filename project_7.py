###### Greater or less

def age_measurement(first_age:int,second_age:int):
    '''this function will measurement of the greater or lesser between two parameters '''
    
    if first_age > second_age:
        return f'ther {first_age} is greater than {second_age}.'
    elif first_age == second_age:
        return f'{first_age} and {second_age} are equal to each other.'

    else:
        return f'{first_age} is lesser than {second_age}'

