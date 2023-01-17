
def fahrenheit_to_celsius(t):
    t_celsius = (t_fahrenheit-32)*(5/9)
    return t_celsius

#answer = input('Enter a temperature in Fahrenheit: ')
#t_fahrenheit = float(answer)
#t = fahrenheit_to_celsius(t_fahrenheit)
#print("Celsius: ", t)

def celsius_to_fahrenheit(t):
    t_fahrenheit = (t_celsius*(9/5))+32
    return t_fahrenheit

#answer = input('Enter a temperature in Celsius: ')
#t_celsius = float(answer)
#t = celsius_to_fahrenheit(t_celsius)
#print("Fahrenheit: ", t)

options = ['c', 'f', 'q']

for ask in options:
    ask = input('What unit would you like to convert to? (Type c or f) ')
    if ask == 'c':
        def fahrenheit_to_celsius(t):
            t_celsius = (t_fahrenheit-32)*(5/9)
            return t_celsius
        answer = input('Enter a temperature in Fahrenheit: ')
        t_fahrenheit = float(answer)
        t = fahrenheit_to_celsius(t_fahrenheit)
        print("Celsius: ", t)
        
    elif ask == 'f': 
        def celsius_to_fahrenheit(t):
            t_fahrenheit = (t_celsius*(9/5))+32
            return t_fahrenheit

        answer = input('Enter a temperature in Celsius: ')
        t_celsius = float(answer)
        t = celsius_to_fahrenheit(t_celsius)
        print("Fahrenheit: ", t)
    elif ask == 'q':
       quit
