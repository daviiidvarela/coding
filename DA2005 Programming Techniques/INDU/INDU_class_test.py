class train_sim:
    def __init__(self):
        self.data = {}
        self.stops = set()
        self.connections = ""

    def station_check(self):
        stations = input("Enter name of stations file: ")
        while True:
            try:
                with open(stations, 'r') as h:
                    '''
                    Opens the specified file and goes line by line to add entries in the new dictionary called 'data'
                    '''
                    for line in h:
                        try:
                            location, delay_prob = line.strip().split(',')
                            delay_prob = float(delay_prob)
                            if isinstance(location, int):
                                raise TypeError("There is row that contains an integer in the location column, the location column can only contain letters or words.")
                            if 0 <= delay_prob <= 1:
                                if location not in self.stops:
                                    self.stops.add(location)
                                if not location in self.data:
                                   self.data[location] = []
                                self.data[location]+= [(float(delay_prob))]
                        except TypeError as e:
                            print("Warning:", e)
                            continue
                return self.data

            except FileNotFoundError: # When FileNotFoundError arrises, then the program asks the user to put in another file name
                print("File not found, please input another file name.") 
                stations = input('Enter name of stations file: ')
                continue
            break

    def connections_check(self):
        self.connections = input("Enter name of connections file: ")    
        while True:
            try:
                with open(self.connections, 'r') as h:
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
                self.connections = input('Enter name of connections file: ')
                continue
            break

    def trains_check(self):
        while True:
            trains = input("Enter how many trains to simulate: ")
            try:
                self.integer_input = int(trains)
            except ValueError:
                print("Invalid input. Please enter an integer.")
            return self.integer_input
    
    def create_trains(self):
        import random
        trains = self.integer_input
        stations = self.data
        train_dict = {}
        for i in range(1, trains+1):
            station = random.choice(list(stations.keys()))
            train_dict[f"train{i}"] = station
        print(train_dict)


def traincode():
    train_functions = train_sim()
    train_functions.station_check()
    train_functions.connections_check()
    train_functions.trains_check()
    train_functions.create_trains()


traincode()