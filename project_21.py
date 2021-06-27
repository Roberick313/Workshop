def Lower_Upper(input_str): 
    """This Function will return the vice versa of the entered sentence"""
    try:
        
        result = ''
        My_dict={
            65:97, 66:98,
            67:99, 68:100,
            69:101, 70:102,
            71:103, 72:104,
            73:105, 74:106,
            75:107, 76:108,
            77:109, 78:110,
            79:111, 80:112,
            81:113, 82:114,
            83:115, 84:116,
            85:117, 86:118,
            87:119, 88:120,
            89:121, 90:122,
        }
        for i in input_str: 

            if 65<= ord(i)<=90: 
                result += chr(My_dict[ord(i)])

            elif 97 <= ord(i) <= 122: 

                for key, value in My_dict.items():
                   
                    if value == ord(i):
                        result += chr(key)  

            else:
                result += i
    except TypeError or ValueError :

        return f'''You entered wrong value.
        \rpls Enter a sentence For example:
        \r"RoberIcK" '''

    except:
        return f'what the hell did you entered??!? :))'
    
    return result

