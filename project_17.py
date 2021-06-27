
from reversestr import FirstReverse as rev

def check_heart1(*t): # ('amin','bob','rar')
    '''this func will find those values that are same as they 
       are when write reversedand if that true will return them.'''

    n = ''
    l = []
    s = rev # my reverse func

    if (type(t) is list) or (type(t) is tuple): # type(t):tuple >> True

        length = len(t)
        
        for i in range(length): # i=1 >> t = ('amin','bob','rar')

            n = t[i] # t[2] =>  'bob'

            if type(n)  is  str: # i = 'bob' type : str. <<the condition is True>>
                
                if n == s(n): # n=bob == reverse('bob') <<True>>

                    l += [s(n)] # l = ['bob']
                    
                else:
                    continue
                
            else: # n = 'bob' type : str <<False>>

                return '''one or all values in iterable are not string!
(your iterable needs to have all its values in str)'''

        return tuple(l)
  
    else: 
        return ('the entery value is not string or iterabale')

#print(check_heart1('rar','ror','bob','gog'))
#################################################################

def check_heart2(*t): # ('amin','bob','rar')
    '''this func will find those values that are same as they 
       are when write reversed and if that's true will return them.'''
    s= ''
    n = ''
    l = []
    l2 = []
    if (type(t) is list) or (type(t) is tuple): # type(t):tuple >> True

        length = len(t)
        
        for i in range(length): # i=1 >> t = ('amin','bob','rar')

            n = t[i] # t[2] =>  'bob'
            
            if type(n)  is  str: # i = 'bob' type : str. <<the condition is True>>
                
                l2 = list(reversed(n))
                length2 = len(l2)
                for i3 in l2:
                    
                    s += i3

                if n == s: # n=bob == reverse('bob') <<True>>

                    l += [s] # l = ['bob']

                    s = ''
                else:
                    continue
                
            else: # n = 'bob' type : str <<False>>

                return '''one or all values in iterable are not string!
(your iterable needs to have all its values in str)'''

        return tuple(l)
  
    else: 
        return ('the entery value is not string or iterabale')
   

b = ('nurses run','ror','bob','gog')
print(check_heart2(*b))
