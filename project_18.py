def myFanc18 (*a):
    ''' This function will devide the arg to 3 that if the arg is
    multiple of 3, the function will return the character of ascci code 
    of the args that how many times the args devided to 3 untill it reachs to 0 (zero)
    and print out the char...
    for example the arg is 66, it devide to 3, 3 times till reach to 0
    then in output we have 3x 'B' char '''
    
    for i in a:

        if i % 3 == 0:
            # b += [i]
            
            def inner_18(s):
                d = 0
                i2 = s
                while True:
                    s /= 3
                    
                    if s <= 1:
                        d2 = d
                        d = 0
                        break
                    else:
                        d += 1
                        
                print(f'{i2} is devided {d2} times thats = {d2*chr(i2)}')
                
            inner_18(i)        

    return 'Done! :)'

# c = list(range(65,124))
# print(myFanc18(*c))