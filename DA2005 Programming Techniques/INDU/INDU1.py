
def station_check():
    stations = input("Enter name of stations file: ")
    data = dict()               
    while True:
        try:
            with open(stations, 'r') as h:
                '''
                Opens the specified file and goes line by line to add entries in the new dictionary called 'data'
                '''
                for line in h:
                    try:
                        location, delay_prob = line.strip().split(',')
                        delay_prob = int(float(delay_prob))
                        if isinstance(location, int):
                            raise TypeError("There is row that contains an integer in the location column, the location column can only contain letters or words.")
                        if 0 <= delay_prob <= 1:
                            pass
                        if not location in data:
                            data[location] = []
                        data[location] += [(float(delay_prob))]
                    except TypeError as e:
                        print("Warning:", e)
                        continue
                    
        except FileNotFoundError: # When FileNotFoundError arrises, then the program asks the user to put in another file name
            print("File not found, please input another file name.") 
            stations = input('Which csv file should be analyzed? ')
            continue
        break

def connections_check():
    connections = input("Enter name of connections file: ")    
    while True:
        try:
            with open(connections, 'r') as h:
                '''
                Opens the specified file and goes line by line to add entries in the new dictionary called 'data'
                '''
                for line in h:
                    try:
                        start_connection, end_connection, line_color, direction = line.strip().split(',') 
                        if isinstance(start_connection or end_connection or line_color or direction, int):
                            raise TypeError("There is row that contains an integer in one of the columns, the connections columns can only contain letters or words.")
                    except TypeError as e:
                        print("Warning:", e)
                        continue
                    
        except FileNotFoundError: # When FileNotFoundError arrises, then the program asks the user to put in another file name
            print("File not found, please input another file name.") 
            connections = input('Which csv file should be analyzed? ')
            continue
        break

def trains_check():
    trains = input("Enter how many trains to simulate: ")
    while True:
        try:
            if isinstance(trains, str):
                raise TypeError("Your input is not an integer, please input a valid value")
        except TypeError as e:
            print("Warning:", e)
            continue




#from random import random

# how to make an if statement that checks if a variable is an integer? 

def train_code():
    station_check()
    connections_check()

train_code()


