a = 9
b = 3
def devider()-> int:

    global a,b
    # a = int(input("enter ur first number: "))
    # b = int(input('enter ur second number: '))
    if b == 0:
        return f'you must enter a number greater than zero(0)!'

    else:
        return a/b

def my_decorator(func):
    
    def my_inner():

        return func()

    return my_inner

my_decor = my_decorator(devider)
