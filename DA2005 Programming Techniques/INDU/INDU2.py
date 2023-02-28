
def station_check():
    stations = input("Enter name of stations file: ")
    data = []
    stops = set()
    while True:
        try:
            with open(stations, 'r') as h:
                '''
                Opens the specified file and goes line by line to add entries in the new dictionary called 'data'
                '''
                for line in h:
                    try:
                        location, delay_prob = line.split(',')
                        delay_prob = float(delay_prob)
                        if isinstance(location, int):
                            raise TypeError("There is row that contains an integer in the location column, the location column can only contain letters or words.")
                        if 0 <= delay_prob <= 1:
                            if location not in stops:
                                stops.add(location)
                                data[location] = []
                                data[location].append(delay_prob)
                        #if not location in data:
                        #   data[location] = []
                        #data[location]+= [(float(delay_prob))]
                    except TypeError as e:
                        print("Warning:", e)
                        continue
            return data
            
                    
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
    while True:
        trains = input("Enter how many trains to simulate: ")
        try:
            integer_input = int(trains)
            return integer_input
        except ValueError:
            print("Invalid input. Please enter an integer.")
        return integer_input


import random

def create_trains():
    trains = trains_check()
    stations = station_check()
    for i in range(1, trains+1):
        stations = random.choice(list(stations.keys()))
        var_name = "train" + str(i)
        exec(var_name + " = '" + stations + "'")
    return locals()






def train_code():
    station_check()
    connections_check()
    trains_check()

#create_trains()
let = station_check()
print(let)
#train_code()


