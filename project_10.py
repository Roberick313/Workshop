#######  finding The Greatest and The least Number with For and while loop


a = [20,10,60,45,100,35,78,37,71,53,8.53,47,23.4,74,89,345,123,68,72.34,34.312]

MinNumber = a[0]

MaxNumber = a[0]

for FirstVal in a:
    
    if MaxNumber < FirstVal:
        
        MaxNumber = FirstVal
        
    elif MinNumber > FirstVal:

        MinNumber = FirstVal
       
print('the Greatest number is: {} and the Least Number is: {}'.format(MaxNumber,MinNumber))
    
    
print("############ 'same programm with while' #################")

MinNumber_while = a[0]

MaxNumber_while = a[0]

Len_a = len(a)
Loop_a = 0

while Loop_a < Len_a:
    Index_counter = a[Loop_a]
    Loop_a += 1 
    if MaxNumber_while < Index_counter:
        
        MaxNumber_while = Index_counter
        
    elif MinNumber_while > Index_counter:

        MinNumber_while = Index_counter
       
print('the Greatest number is: {} and the Least Number is: {}'.format(MaxNumber_while,MinNumber_while))
