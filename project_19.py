
from Myseprator import MySeparator
try:
        
    def char_and_ascci(character = '65 66 67', ordy = 'xyz'): # // input >> msd = '66 87 70' , asd = ' abc'
        ''' < character = '66 67 78'  \\  ord = 'xyz' >  
            \n this function will return the character of ascci number of character parameter and
        the ascci code of ordy parameter... '''
        asci = ''

        l1 = MySeparator(character) 

        ordi = ''

        l2 = list(ordy) 

        #print(l1,l2) ## ['65', '66', '67'] ['x', 'y', 'z']
            
        for i in l1: # l1 = ['65', '66', '67']
                
            asci += chr(int(i)) # asci = 'A'
                
            
        for i2 in l2:
                
            ordi += str(ord(i2))+' ' # ordi = 120
                
            
        return f"1.{asci} \n2.{ordi}"

except :
    print(f'read the info of function. in case the function dont work, report it to Roberick313@gmailc.com')

#print(char_and_ascci(character='76 98 47 76',ordy= 'xsdfw'))