from Myseprator import MySeparator as MS

def main(Bo_aza):
    ''' This Function will return the ascci code of characters and
character of numbers that has given to it.
________________________

For call the function you need to enter a single string that can contain numbers and character.
for example: main("57 67 39 67 213 Roberick")'''
    number = ''
    chararacter = ''
    sepi = MS(Bo_aza) # ['amin', '65', '75', '86']
    
    def my_ord(i): 

        nonlocal number
        number += chr(int(i))+ ' '
        return number

    def my_char(i):     
                
        nonlocal chararacter
        for ss in i:
            chararacter += str(ord(ss)) + ' '
        return chararacter

    for i in sepi: 
        
        try:

            if int(i):
                my_ord(i)

        except:

            my_char(i)
            
    return f'"({Bo_aza})" converted to: \nnumbers are:"{number}" \ncharacters are:"{chararacter}".'

print(main('amin ansari 65 114'))
