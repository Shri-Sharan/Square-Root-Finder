#This code works for all +ve non-zero integers only!! Uses manual Long division method like humans do instead of Newton's babylion formula.                                                                                                                       '''tintin's code'''
#You can import the module and call this on an integer or call the function empty to enter input
#Code is 100% AI free and tested for accuracy on several test cases
'''Square root by Long Division Method'''

def square_root(user_input=None):
 """tintin's code"""
 if user_input == None:
  y = True
  while y:
     try:
          user_input = int(input('Please enter Integers only!: '))
          if type(user_input) is int:
               y = False
     except:
           print('Integers only allowed no float or strings!!')
               
 if user_input:
    
    if type(user_input) is int: 
            user_input = int(user_input)

    else :
        raise TypeError('input must be integers only!') 
    

    #user_input = int(user_input)
    string_of_input = str(user_input)
    list_input = list(string_of_input)
    input_length = len(string_of_input)
    input_pairs = []
    quotient = []
    #upto decimal points input

    remainder = 0

    if input_length % 2 != 0:
        input_pairs.append(list_input[0])
        del (list_input[0])
        input_length -= 1
        
        tot_no_of_pairs = (input_length // 2) + 1
    else :
        tot_no_of_pairs = input_length // 2

    no_of_2digit_pairs = input_length // 2
    for xi in range(0,no_of_2digit_pairs):
        a = list_input[0] + list_input[1]
        input_pairs.append(a)
        del list_input[0:2]


    tot_no_of_divisions = tot_no_of_pairs
    dividend = input_pairs
    divisor = '0'

#Tintin's code
    while tot_no_of_divisions:
    #for i in range(0,3):
        squares =  list((int((divisor) + str(x)), int((divisor) + str(x))*x) for x in range(0,10))
        #if dividend:

        temp_dividend = int(dividend[0])
        for xi in squares:
            
            if (xi[1] == temp_dividend):
                temp_quotient = xi[1] // xi[0] 
                remainder = 0
                break

            elif xi[1] < temp_dividend:
                try:
                    temp_quotient = xi[1] // xi[0] 
                except:
                    continue
                remainder = temp_dividend - xi[1]
                

        quotient.append(temp_quotient)
        quotient_for_divisor_calculation = ''.join(str(x) for x in quotient)
        if '.' in quotient_for_divisor_calculation:
            quotient_for_divisor_calculation = quotient_for_divisor_calculation.replace('.','')

        divisor = str(2 * int(quotient_for_divisor_calculation))


        tot_no_of_divisions -=1

        if (tot_no_of_divisions == 0) and (remainder != 0) and ((tot_no_of_divisions) < (tot_no_of_pairs + 10)):
                    tot_no_of_divisions += 10
                    tot_no_of_pairs = -10
                    zeroes = []
                    str00 = '00'
                    for ix in range(0,10):
                        zeroes.append(str00)
                    dividend += zeroes
                    quotient.append('.')

        
        try:
            dividend.insert(0, (str(remainder)+dividend[1]))
        except:
            pass

        

        try:
            del dividend[1:3]
        except:
            pass
        

        
        
        

    final_quotient =''.join(str(x) for x in quotient)
    return (f'Square root of {user_input} is : {final_quotient}')


print(square_root())






























