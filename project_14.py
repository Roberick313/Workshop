#### Simple Calculator

def simple_calculator(first_number,second_number,Operator):

    if Operator == '+':
        Sum = first_number + second_number
        return f'the Division of two numbers is: {Sum}'

    elif Operator == '*':
        Multi = first_number*second_number
        return f'the Division of two numbers is: {Multi}'

    elif Operator == '-':
        Sub = first_number - second_number
        return f'the Division of two numbers is: {Sub}'

    elif Operator == '/':

        Div= first_number / second_number
        return f'the Division of two numbers is: {Div}'
