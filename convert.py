
#def fahrenheit_to_celsius(t):
#    t_celsius_f = (t_fahrenheit-32)*(5/9)
#    return t_celsius_f

#def celsius_to_fahrenheit(t):
#    t_fahrenheit = (t_celsius*(9/5))+32
#    return t_fahrenheit



options = ['c', 'f', 'k', 'q']

for ask in options:
    ask = input('What unit would you like to convert to? (Type c, f or k; or q to quit) ') #4. program asks what the user wants
    if ask == 'q':
       exit() #5. continues until user quits
    elif ask != 'q':
        ask1 = input('What unit are you converting from? (Type c, f or k) ')
    if ask == 'c':
        def to_celsius(t):
            t_celsius_f = (t_fahrenheit-32)*(5/9) #2. fahrenheit_to_celsius fixed
            t_celsius_k = (t_kelvin-32)*(5/9)
            return t_celsius_f
            return t_celsius_k
        if ask1 == 'f':
            answer = input('Enter a temperature in Fahrenheit: ')
        elif ask1 == 'k':
            answer = input('Enter a temperature in Kelvin: ')
        t_fahrenheit = float(answer)
        t = to_celsius(t_fahrenheit)
        print("Celsius: ", t)
        
    elif ask == 'f': 
        def celsius_to_fahrenheit(t):
            t_fahrenheit = ((t_celsius*(9/5))+32) #3. program extended to do other conversion
            return t_fahrenheit

        answer = input('Enter a temperature in Celsius: ')
        t_celsius = float(answer)
        t = celsius_to_fahrenheit(t_celsius)
        print("Fahrenheit: ", t)
    
    elif ask != 'q' or ask!= 'c' or ask!= 'f' or ask != 'k' or ask1!= 'c' or ask1!= 'f' or ask1!= 'k':
        print('Please input a valid option')
