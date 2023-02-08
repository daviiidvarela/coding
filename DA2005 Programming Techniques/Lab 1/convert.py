
def fahrenheit_to_celsius(t): #2. fahrenheit_to_celsius calculates correctly
    t_celsius_f = (t_fahrenheit-32)*(5/9)
    return t_celsius_f

def celsius_to_fahrenheit(t): #3. program extended to convert from celsius to fahrenheit
    t_fahrenheit_c = (t_celsius*(9/5))+32
    return t_fahrenheit_c

def celsius_to_kelvin(t):
    t_kelvin_c = t_celsius + 273.15
    return t_kelvin_c

def kelvin_to_celsius(t):
    t_celsius_k = t_kelvin - 273.15
    return t_celsius_k

def fahrenheit_to_kelvin(t):
    t_kelvin_f = (t_fahrenheit-32)*(5/9) + 273.15
    return t_kelvin_f

def kelvin_to_fahrenheit(t):
    t_fahrenheit_k = ((t_kelvin - 273.15)*(9/5))+32
    return t_fahrenheit_k

#6. program extended to do all conversions and continues until user inputs q at any point

options = ['c', 'f', 'k', 'q']

while True:
    ask = input('What unit would you like to convert to? (Type c, f or k; or q to quit) ') #4. program asks what the user wants
    if ask == 'q':
       exit() #5. continues until user quits
    elif ask== 'c' or ask== 'f' or ask == 'k' :
        ask1 = input('What unit are you converting from? (Type c, f or k) ')
        if ask1 == 'q':
            exit() #5(extra). user can quit at any point of the choosing of converstion

    if ask == 'c':
        if ask1 == 'f':
            answer = input('Enter a temperature in Fahrenheit: ')
            t_fahrenheit = float(answer)
            t = fahrenheit_to_celsius(t_fahrenheit)
            print("Celsius: ", t)
        elif ask1 == 'k':
            answer = input('Enter a temperature in Kelvin: ')
            t_kelvin = float(answer)
            t = kelvin_to_celsius(t_kelvin)
            print("Celsius: ", t)
        elif ask1!='f' or ask1!='k':
            print('Please input a valid option')

        
    elif ask == 'f': 
        if ask1 == 'c': #3. program extended to convert from celsius to fahrenheit
            answer = input('Enter a temperature in Celsius: ')
            t_celsius = float(answer)
            t = celsius_to_fahrenheit(t_celsius)
            print("Fahrenheit: ", t)
        elif ask1 == 'k':
            answer = input('Enter a temperature in Kelvin: ')
            t_kelvin = float(answer)
            t = kelvin_to_fahrenheit(t_kelvin)
            print("Fahrenheit: ", t)
        elif ask1!='c' or ask1!='k':
            print('Please input a valid option')

    elif ask == 'k': 
        if ask1 == 'c':
            answer = input('Enter a temperature in Celsius: ')
            t_celsius = float(answer)
            t = celsius_to_kelvin(t_celsius)
            print("Kelvin: ", t)
        elif ask1 == 'f':
            answer = input('Enter a temperature in Fahrenheit: ')
            t_fahrenheit = float(answer)
            t = fahrenheit_to_kelvin(t_fahrenheit)
            print("Kelvin: ", t)
        elif ask1!='c' or ask1!='f':
            print('Please input a valid option')

    
    elif ask != 'q' or ask != 'c' or ask != 'f' or ask != 'k' or ask1!= 'c' or ask1!= 'f' or ask1!= 'k':
        print('Please input a valid option')
