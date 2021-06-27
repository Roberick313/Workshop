def my_reverse(entry_parameter) -> str:
    """this function will reverse the word or sentence
    that it takes"""

    counter = len(entry_parameter)-1
    string = ''

    while counter >= 0:
        string += entry_parameter[counter]
        counter -= 1

    return string
