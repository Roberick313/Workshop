def counting_str(entry_parameter):
    """This function will return the index and
the Repeated time of roberick in the entered sentence """

    counter_test = 0
    sentence = ''
    counter_char = 0

    try:
        # checking the length of the Input...
        if len(entry_parameter) < 10:
            entry_parameter = 'python language tutorials by roberick'
            print(f'''you entered a sentence less than 10 character.
            \rthe default sentence is:
            \r"python language tutorials by roberick"''')
            
        # I used my own module to separate the sentence to a list
        cup_1 = my_separator(entry_parameter)
    
        # this loop is just to count the repeated time
        # of roberick in the sentence
        for i in cup_1:
            if i.lower() == 'roberick':
                counter_char += 1

        # this loop here is to find out the index of the first
        # roberick in the sentence
        for i2 in entry_parameter:
            sentence += i2
            counter_test += 1

            # to find the roberick and its index
            if 'roberick' in sentence.lower():
                counter_test = counter_test - 8
                break
            
            # this condition is for clear the
            # sentence variable
            if i2 == ' ':
                sentence = ''
                continue
    
    except ValueError:
        return f'You Enter wrong value. Pls try again!'
    except TypeError:
        return f'you have to enter character not int or any numerical...'

    return f'''Repeated time of roberick: {counter_char}
    \rthe index of first roberick in this sentence: {counter_test}'''


def my_separator(character):
    """This function will seperate the entry string"""

    l1 = []
    ss = ''
    counter = 0

    for i in character:

        if i == ' ':
            l1.append(ss)
            ss = ''
            counter += 1

        elif counter == len(character) - 1:

            ss += i
            l1.append(ss)
            ss = ''

        else:
            ss += i
            counter += 1

    return l1
