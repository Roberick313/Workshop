## find the number of the repetition of vowel sound words in a sentence
### without using string functions

#sentence = str(input('enter your sentence: '))
def vowel_sound(word):
    '''this function will count the number of vowel sound that used\n
    \rin the sentence "paratmeter"'''

    a = 0 
    e = 0 
    i = 0 
    o = 0 
    u = 0 

    for first_for in word:
        
        if first_for == 'a' or first_for == 'A':
            a += 1
        elif first_for == 'e' or first_for == 'E':
            e += 1
        elif first_for == 'i' or first_for == 'I':
            i += 1
        elif first_for == 'o' or first_for == 'O':
            o += 1
        elif first_for == 'u' or first_for == 'U':
            u += 1
        
    return f'a: {a}\ne: {e}\ni: {i}\no: {o}\nu: {u}'

