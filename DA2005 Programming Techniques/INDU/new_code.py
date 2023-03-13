class train_sim:
    def __init__(self):
        self.data = {}
        self.stops = set()
        self.connections = ""
        self.current_time = 0
        self.trains = []

    def station_check(self):
        stations = input("Enter name of stations file: ")
        while True:
            try:
                with open(stations, 'r') as h:
                    data = {}
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
                            self.start_connection, self.end_connection, self.line_color, self.direction = line.strip().split(',') 
                            if isinstance(self.start_connection or self.end_connection or self.line_color or self.direction, int):
                                raise TypeError("There is row that contains an integer in one of the columns, the connections columns can only contain letters or words.")
                        except TypeError as e:
                            print("Warning:", e)
                            continue
                        return self.start_connection, self.end_connection, self.line_color, self.direction

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

        self.train_dict = {}
        for i in range(1, trains+1):
            station = random.choice(list(stations.keys()))
            line_color = random.choice(self.line_color)
            direction = random.choice(self.direction)
        
        # Add train to the dictionary
            self.train_dict[f"Train{i}"] = {'station': station, 'line_color': line_color, 'direction': direction}
            

            #self.train_dict[f"Train{i}"] = station
            
        print(self.train_dict)

    def user_decision(self):
        try:
            while True:
                user_decision = input('Continue simulation [1], train info [2], exit [q]: ')
                if user_decision == 1:
                    self.move_trains()
                elif user_decision == 2:
                    self.train_info()
                elif user_decision == 'q':
                    print("Thank you and goodbye!")
                    break
        except TypeError as e:
            print("Warning:", e)
        

            
    def move_trains(self):
        import random
        for train in self.trains:
            current_location, current_direction = train
            possible_destinations = []
            for neighbor, line, direction in self.connections[current_location]:
                if current_direction == direction:
                    possible_destinations.append((neighbor, line, direction))
            if len(possible_destinations) == 0:
                current_direction = "N" if current_direction == "S" else "S"
                train = (current_location, current_direction)
            else:
                next_location, line, direction = random.choice(possible_destinations)
                if next_location in self.final_stops:
                    current_direction = "N" if current_direction == "S" else "S"
                else:
                    delay_prob = self.data[next_location]
                    if random.random() < delay_prob:
                        next_location = current_location
                self.train = (next_location, current_direction)

    def train_info(self):
        import random
        train_num = int(input("Which train [1 - {}]: ".format(len(self.train_dict))))
        train = self.train_dict[train_num - 1]
        print("{} on {} line is at station {} heading in {} direction{}.".format(
            train[0], train['line'], train['station'], train['direction'],
            " (DELAY)" if random.random() < 0.2 else ""))

def traincode():
    train_functions = train_sim()
    train_functions.station_check()
    train_functions.connections_check()
    train_functions.trains_check()
    train_functions.create_trains()
    train_functions.user_decision()
    train_functions.move_trains()
    #train_functions.train_info()


traincode()